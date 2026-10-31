# AnimalCards · 常见动物卡

一张卡一种动物，仿宝可梦卡牌的竖版布局，沿用 OrangeSTEM 海报的 v4 网格线 + 等轴线稿风格。

## 卡片列表

| 编号 | 名字 | 类别 | IUCN | 图片链接 |
|---|---|---|---|---|
| 001 | 大熊猫（Giant panda） | 森林 | VU 易危 | [PNG](%E5%8A%A8%E7%89%A9/%E6%A3%AE%E6%9E%97/%E5%A4%A7%E7%86%8A%E7%8C%AB.png) · [PDF](%E5%8A%A8%E7%89%A9/%E6%A3%AE%E6%9E%97/%E5%A4%A7%E7%86%8A%E7%8C%AB.pdf) |
| 002 | 家猫（Domestic cat） | 宠物 | NE 未评估（家养） | [PNG](%E5%8A%A8%E7%89%A9/%E5%AE%A0%E7%89%A9/%E5%AE%B6%E7%8C%AB.png) · [PDF](%E5%8A%A8%E7%89%A9/%E5%AE%A0%E7%89%A9/%E5%AE%B6%E7%8C%AB.pdf) |
| 003 | 非洲象（African bush elephant） | 高原草原 | EN 濒危 | [PNG](%E5%8A%A8%E7%89%A9/%E9%AB%98%E5%8E%9F%E8%8D%89%E5%8E%9F/%E9%9D%9E%E6%B4%B2%E8%B1%A1.png) · [PDF](%E5%8A%A8%E7%89%A9/%E9%AB%98%E5%8E%9F%E8%8D%89%E5%8E%9F/%E9%9D%9E%E6%B4%B2%E8%B1%A1.pdf) |
| 004 | 帝企鹅（Emperor penguin） | 鸟类 | NT 近危 | [PNG](%E5%8A%A8%E7%89%A9/%E9%B8%9F%E7%B1%BB/%E5%B8%9D%E4%BC%81%E9%B9%85.png) · [PDF](%E5%8A%A8%E7%89%A9/%E9%B8%9F%E7%B1%BB/%E5%B8%9D%E4%BC%81%E9%B9%85.pdf) |
| 005 | 章鱼（Common octopus） | 海洋 | LC 无危 | [PNG](%E5%8A%A8%E7%89%A9/%E6%B5%B7%E6%B4%8B/%E7%AB%A0%E9%B1%BC.png) · [PDF](%E5%8A%A8%E7%89%A9/%E6%B5%B7%E6%B4%8B/%E7%AB%A0%E9%B1%BC.pdf) |
| 006 | 狮子（Lion） | 高原草原 | VU 易危 | [PNG](%E5%8A%A8%E7%89%A9/%E9%AB%98%E5%8E%9F%E8%8D%89%E5%8E%9F/%E7%8B%AE%E5%AD%90.png) · [PDF](%E5%8A%A8%E7%89%A9/%E9%AB%98%E5%8E%9F%E8%8D%89%E5%8E%9F/%E7%8B%AE%E5%AD%90.pdf) |

## 说明

- **风格**：1080×1920 竖版卡，浅网格背景、细线等轴插画，颜色只用墨色 + 类型色（陆地绿 / 水中蓝 / 天空青 / 两栖青绿）+ 橙、黄两种点缀色。每张卡都输出 PNG（2× 分辨率）和单页 PDF。
- **卡片内容**：中英文名 + 拉丁学名、栖息类型和食性标签、IUCN 红色名录等级徽章、4 条“身体数据”条、2 个技能、3 句简介、冷知识和分布。
- **数据条**：只用查得到的真实数据。实心段是 0 到下限，条纹段是常见范围；体重、体长用对数刻度，其余用线性刻度。近似值标“约”，口径（如雌雄合并、野外寿命）写在卡底注释里。
- **数据来源**：英文 Wikipedia 对应条目，IUCN 红色名录（等级和评估年份），部分卡片另用 Smithsonian's National Zoo 等动物园或机构资料。每张卡的底部都列出了它用到的来源。
- **插画**：插画是示意图，不按真实比例。
- **审核**：卡片由 AI 辅助制作，数据和文字**需要人工审核**后再用于教学或印刷。
- **重新生成**：`tools/` 里有模板和脚本。`tools/data/*.json` 存数据，`art.py` 画插画，运行 `python tools/render_card.py` 即可（需要 Playwright + Chrome、Jinja2 和 Noto Sans CJK 字体）。
