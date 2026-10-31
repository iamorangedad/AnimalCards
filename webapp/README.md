# 动物卡片地球（AnimalCards Globe）

把仓库里的 400 张动物卡片放到一个可拖拽、可缩放的 3D 地球上：每种动物在分布地有 1–3 个标注，点击标注会打开卡片预览，可以查看高清 PNG、下载 PDF。

> ⚠️ **数据说明**：标注位置是根据卡片“分布”文字匹配到的国家/区域代表点，**全部是近似位置**，不是真实分布范围。数据由 AI 辅助整理，**需要人工复核**。页面底部和“数据来源”面板里也有同样的说明。

## 功能

- 3D 地球：自动旋转，可拖动、缩放；NASA Blue Marble 贴图，带地形凹凸
- 标注按类别着色，用卡片头像做图标；离得近的标注会自动聚合成气泡，放大后再展开；同一地点的多种动物错开显示，放大后点击气泡会列出这里的全部动物
- 悬停显示名字，点击打开侧栏（手机上是底部抽屉）：卡片缩略图、点开看高清 PNG、下载 PDF、IUCN 等级、分布、标注依据、来源
- 类别筛选、IUCN 等级筛选（Shift/Alt + 点击 = 只看这一项）、搜索（中文/英文/学名），选中后地球会飞到这个动物
- 链接分享：`/#a=giant-panda` 直接打开大熊猫
- 界面全中文，适配手机

## 目录

```
webapp/
├── backend/app.py          FastAPI 服务（API + 静态文件）
├── frontend/               前端（index.html / style.css / app.js；vendor/ 为本地打包的 globe.gl）
├── data/animals.json       由脚本生成的动物+坐标数据（不要手改，改脚本或 locations_manual.json）
├── data/locations_manual.json   人工指定的标注点（附来源）
├── data/gazetteer_ne.json  由 Natural Earth 生成的国家代表点
├── thumbs/                 WebP 缩略图（400px 卡片预览 + 120px 头像），约 12MB
├── scripts/                生成数据和缩略图的脚本
├── tests/                  URL 检查和截图脚本
├── Dockerfile / docker-compose.yml / .env.example
└── deploy/                 nginx 和 systemd 示例
```

卡片原图 PNG/PDF **不复制**，服务直接读取仓库里的 `动物/` 文件夹。

## 本地运行

需要 Python 3.10+。

```bash
cd webapp
python3 -m venv .venv
.venv/bin/pip install -r backend/requirements.txt
cd backend
../.venv/bin/uvicorn app:app --host 127.0.0.1 --port 8000
# 浏览器打开 http://127.0.0.1:8000
```

### 更新数据 / 缩略图（新增或修改卡片之后）

```bash
cd webapp
.venv/bin/pip install -r scripts/requirements-build.txt   # Pillow
python3 scripts/build_data.py            # 读取 ../tools/data/*.json → data/animals.json
.venv/bin/python scripts/build_thumbs.py # 读取 ../动物/**/*.png → thumbs/*.webp（已存在的跳过，--force 全部重做）
# 国家代表点一般不用重做；如需：下载 Natural Earth 1:50m admin0 geojson 后
# python3 scripts/build_gazetteer.py ne_50m_admin_0_countries.geojson
```

### 检查

```bash
.venv/bin/python tests/check_urls.py http://127.0.0.1:8000   # API 是否 400 条、所有 PNG/PDF/缩略图是否可访问
# 截图（需要 playwright 和 Chromium）
python tests/screenshots.py http://127.0.0.1:8000 /tmp/shots [chrome 路径]
```

## API

| 路径 | 说明 |
|---|---|
| `GET /api/animals` | 动物列表。参数：`category`（如 `海洋`，多个用逗号）、`iucn`（如 `CR,EN`）、`q`（名称搜索）、`bbox`（`minLon,minLat,maxLon,maxLat`，支持跨日界线）、`limit`、`offset`。返回 `{count, items}` |
| `GET /api/animals/{id}` | 单个动物，如 `/api/animals/giant-panda` |
| `GET /api/meta` | 数量统计、类别、数据说明 |
| `GET /healthz` | 健康检查 |
| `GET /cards/<类别>/<名字>.png\|.pdf` | 卡片原图 / PDF（来自 `动物/`） |
| `GET /thumbs/<id>_400.webp`、`<id>_120.webp` | 缩略图 |
| `GET /api/docs` | 自动生成的接口文档 |

服务开启了 gzip；卡片、缩略图、贴图带 7 天缓存，API 5 分钟，页面本身 `no-cache`（更新后立即生效）。

## 部署到服务器

### 方式一：Docker（推荐）

```bash
git clone https://github.com/iamorangedad/AnimalCards.git /opt/AnimalCards
cd /opt/AnimalCards/webapp
cp .env.example .env          # 按需改端口
docker compose up -d --build
curl http://127.0.0.1:8000/healthz
```

compose 会把整个仓库**只读**挂载进容器，所以以后更新只需要：

```bash
cd /opt/AnimalCards && git pull && cd webapp && docker compose restart
```

### 方式二：systemd（不用 Docker）

```bash
cd /opt/AnimalCards/webapp
python3 -m venv .venv && .venv/bin/pip install -r backend/requirements.txt
cp .env.example .env   # 把 ANIMALCARDS_ROOT 改成 /opt/AnimalCards
sudo cp deploy/animalcards.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now animalcards
```

### 域名和 HTTPS（nginx）

```bash
sudo cp deploy/nginx.conf /etc/nginx/sites-available/animalcards   # 改 server_name
sudo ln -s /etc/nginx/sites-available/animalcards /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
sudo certbot --nginx -d 你的域名
```

资源占用很小：每个 uvicorn 进程约 60MB 内存；单个页面首次加载约 4MB（地球贴图 1.5MB + globe.gl 1.9MB），之后走缓存。

## 坐标数据是怎么来的（请复核）

`scripts/build_data.py` 读取每张卡片的“分布”文字（`tools/data/*.json` 的 `range` 字段）：

1. 按标点切分句子，丢掉“引入 / 养殖 / 入侵 / 已被带到…”这类非原生分布的句子，去掉“…除外”；
2. 在句子里找国家名（Natural Earth 中文名）、大洲/地区、省份、海域等关键词，取最长匹配；国家后面跟“北部/东南部”等方位时，按国界范围推算一个点；
3. 海洋动物优先放海里，陆地动物优先放陆地；相距不到 400km 的点合并；每种最多 3 个点；
4. 文字里只有“全球 / 广泛分布 / 除南极洲外”的，放 3 个代表点并标“广泛分布”；
5. 家养动物标在**驯化起源地**；有 7 种（北极熊、雪鸮、狗、马、骡、家鸽、花枝鼠）用了人工点位，写在 `data/locations_manual.json`，每条都附维基百科来源。

当前结果：400 种全部有标注，共 822 个点，**全部 `approx: true`**；
- 361 种由分布文字自动匹配，7 种人工点位，32 种只有“广泛分布”代表点；
- `宠物小鼠` 的驯化起源没有找到可靠来源，标为“驯化起源待核”；
- 另有 9 种卡片的分布文字本身含“待核”（狗、红袋鼠、赤狐、浣熊、宠物小鼠、豌豆蚜、亮斑扁角水虻、普通草蛉、蜉蝣）。

每个点在数据里都带 `kind`（标注依据）、`label`，每种动物带 `range_note`、`source`（维基百科条目）和 `location_method`，页面侧栏会显示这些信息和复核提示。

## 第三方资源和许可证

| 资源 | 许可证 |
|---|---|
| [globe.gl](https://github.com/vasturiano/globe.gl) 2.46（含 three-globe） | MIT，见 `frontend/vendor/LICENSE-*.txt` |
| [three.js](https://threejs.org/) | MIT |
| 地球贴图 `earth-blue-marble.jpg`、`earth-topology.png`（来自 three-globe 示例，源自 NASA Blue Marble / NASA 地形数据） | 公有领域（NASA） |
| [Natural Earth](https://www.naturalearthdata.com/) 1:50m 国家边界（用于生成 `gazetteer_ne.json`） | 公有领域 |
| FastAPI / Uvicorn | MIT / BSD-3 |

前端不依赖任何运行时 CDN，所有文件都在本地。
