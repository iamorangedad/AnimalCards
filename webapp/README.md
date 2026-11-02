# AnimalCards Globe

**English** · [中文 (Chinese)](README.zh-CN.md) · [Back to the main README](../README.md)

A draggable, zoomable 3D globe showing all 1000 cards in this repository (760 animals, 200 plants, 40 fungi). Each species has one to three markers where it lives or comes from. Click a marker to preview the card, open the full PNG or download the PDF.

> ⚠️ **About the data:** markers are representative points for the countries or regions matched from each card's range text. They are **all approximate** and are not real distribution ranges. The data was compiled with AI assistance and **needs human review**. The page footer and the “Data & sources” panel say the same. Open location issues are listed in section 4 of [REVIEW_CHECKLIST.md](../REVIEW_CHECKLIST.md#4-web-app-map-locations).

## Features

- **3D globe** that auto-rotates and can be dragged and zoomed, using the NASA Blue Marble texture with terrain bump.
- **Markers** coloured by category, using the card avatar as the icon.
  - Nearby markers merge into clusters that split apart as you zoom in.
  - Species at the same spot are offset. When zoomed in, clicking a cluster lists every species there.
- **Hover** shows the name. **Click** opens a side panel (a bottom drawer on phones) with:
  - the card thumbnail, a full-size PNG view and a PDF download
  - IUCN status, range, how the location was chosen, and sources
- **Filters and search**
  - Kingdom filter: click Animals / Plants / Fungi to show only that kingdom, click again to show all.
  - 16 category filters, each with its own colour (8 animal, 6 plant, 2 fungus).
  - IUCN filter: Shift/Alt-click shows only that category.
  - Search by Chinese, English or scientific name; picking a result flies the globe to that species.
- **Shareable links**: `/#a=giant-panda` opens the giant panda directly.
- **Language toggle**: the UI is Chinese by default. The **EN / 中文** button in the top bar switches to English, and the choice is saved in the browser; `?lang=en` also works. In English mode names, categories, IUCN labels and all UI text are English. Range texts and place labels come from the Chinese cards, so they stay in Chinese.
- **Mobile-friendly**.

## Layout

```
webapp/
├── backend/app.py          FastAPI service (API + static files)
├── frontend/               front end (index.html / style.css / app.js; vendor/ holds a bundled globe.gl)
├── data/animals.json       generated species + coordinates (don't edit by hand; edit the scripts or locations_manual.json)
├── data/locations_manual.json   hand-placed markers (with sources)
├── data/gazetteer_ne.json  country label points generated from Natural Earth
├── thumbs/                 WebP thumbnails (400 px card preview + 120 px avatar, 2000 files), about 30 MB
├── scripts/                scripts that build the data and thumbnails
├── tests/                  URL check and screenshot scripts
├── Dockerfile / Dockerfile.k8s / docker-compose.yml / .env.example
└── deploy/                 nginx, systemd, and Kubernetes (kustomize) examples
```

Card PNG/PDF files are **not copied**. The service reads them straight from the repository's `动物/` (animals), `植物/` (plants) and `真菌/` (fungi) folders, under the URL prefixes `/cards/`, `/plants/` and `/fungi/`. The environment variables `CARDS_DIR`, `PLANTS_DIR` and `FUNGI_DIR` change these paths.

## Run locally

Requires Python 3.10+.

```bash
cd webapp
python3 -m venv .venv
.venv/bin/pip install -r backend/requirements.txt
cd backend
../.venv/bin/uvicorn app:app --host 127.0.0.1 --port 8000
# open http://127.0.0.1:8000  (English UI: http://127.0.0.1:8000/?lang=en)
```

### Rebuild data and thumbnails (after adding or changing cards)

```bash
cd webapp
.venv/bin/pip install -r scripts/requirements-build.txt   # Pillow
python3 scripts/build_data.py            # reads ../tools/data/*.json → data/animals.json
.venv/bin/python scripts/build_thumbs.py # reads ../动物|植物|真菌/**/*.png → thumbs/*.webp (skips existing; --force redoes all)
# Country points rarely need rebuilding; if they do, download the Natural Earth 1:50m admin0 geojson, then:
# python3 scripts/build_gazetteer.py ne_50m_admin_0_countries.geojson
```

### Checks

```bash
.venv/bin/python tests/check_urls.py http://127.0.0.1:8000   # API returns 1000 items; every PNG/PDF/thumbnail is reachable
# screenshots (needs playwright and Chromium)
python tests/screenshots.py http://127.0.0.1:8000 /tmp/shots [path-to-chrome]
```

## API

| Path | Description |
|---|---|
| `GET /api/animals` | Card list (animals, plants and fungi; the endpoint name is kept for compatibility). Parameters: `category` (Chinese category name, e.g. `海洋` Ocean, `蘑菇` Mushrooms; comma-separated), `iucn` (e.g. `CR,EN`), `q` (name search), `bbox` (`minLon,minLat,maxLon,maxLat`, antimeridian-safe), `limit`, `offset`. Returns `{count, items}` |
| `GET /api/animals/{id}` | One species, e.g. `/api/animals/giant-panda` |
| `GET /api/meta` | Counts, categories, data notes |
| `GET /healthz` | Health check |
| `GET /cards/<category>/<name>.png\|.pdf` | Animal card image / PDF (from `动物/`) |
| `GET /plants/<category>/<name>.png\|.pdf` | Plant cards (from `植物/`) |
| `GET /fungi/<category>/<name>.png\|.pdf` | Fungus cards (from `真菌/`) |
| `GET /thumbs/<id>_400.webp`, `<id>_120.webp` | Thumbnails |
| `GET /api/docs` | Auto-generated API docs |

Each item has `name_zh`, `name_en`, `latin`, `kingdom`, `category` (Chinese), `iucn`, `range_text`, `locations[]` and the card URLs. Responses are gzip-compressed. Cards, thumbnails and textures are cached for 7 days and the API for 5 minutes. The page itself is `no-cache`, so updates show up immediately.

## Deploying to a server

### Option 1: Kubernetes (one-shot)

Self-contained image (cards baked in; no host mounts). From the repository root:

```bash
# build + kubectl apply (needs docker and kubectl)
./webapp/deploy/k8s/deploy.sh

# or step by step:
docker build -f webapp/Dockerfile.k8s -t animalcards-globe:k8s .
# kind: kind load docker-image animalcards-globe:k8s
# minikube: minikube image load animalcards-globe:k8s
kubectl apply -k webapp/deploy/k8s/
kubectl -n animalcards port-forward svc/animalcards-globe 8000:80
```

To a registry: `IMAGE=ghcr.io/YOUR_ORG/animalcards-globe:k8s ./webapp/deploy/k8s/deploy.sh`. See [deploy/k8s/README.md](deploy/k8s/README.md).

### Option 2: Docker Compose

```bash
git clone https://github.com/iamorangedad/AnimalCards.git /opt/AnimalCards
cd /opt/AnimalCards/webapp
cp .env.example .env          # change the port if needed
docker compose up -d --build
curl http://127.0.0.1:8000/healthz
```

Compose mounts the whole repository **read-only** into the container, so updating later only needs:

```bash
cd /opt/AnimalCards && git pull && cd webapp && docker compose restart
```

### Option 3: systemd (no Docker)

```bash
cd /opt/AnimalCards/webapp
python3 -m venv .venv && .venv/bin/pip install -r backend/requirements.txt
cp .env.example .env   # set ANIMALCARDS_ROOT to /opt/AnimalCards
sudo cp deploy/animalcards.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now animalcards
```

### Domain and HTTPS (nginx)

```bash
sudo cp deploy/nginx.conf /etc/nginx/sites-available/animalcards   # edit server_name
sudo ln -s /etc/nginx/sites-available/animalcards /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
sudo certbot --nginx -d your.domain
```

Resource use is small. Each uvicorn process takes about 60 MB of RAM. The first page load is about 4 MB (1.5 MB globe texture + 1.9 MB globe.gl), and later loads come from the cache.

## How the coordinates are made (please review)

`scripts/build_data.py` reads each card's range text (the `range` field in `tools/data/*.json`):

1. It splits the text into sentences. It drops sentences about non-native occurrence (“introduced / farmed / invasive / brought to …”) and removes “… excluded” clauses.
2. It looks for country names (Natural Earth Chinese names), continents and regions, provinces, seas and other keywords, and takes the longest match. When a country is followed by a direction such as “northern” or “south-eastern”, it estimates a point inside the country's extent.
3. Marine animals and seagrasses (eelgrass, Neptune grass) are placed at sea first and everything else on land first. Points less than 400 km apart are merged, with at most 3 points per species.
4. Texts that only say “global / widespread / everywhere except Antarctica” get 3 representative points marked “widespread”.
5. Domestic animals are placed at their **domestication centre**. Cultivated plants and cultivated mushrooms (72 species, `cultivated: true` in the data) are placed at their **origin**, not across all growing areas.
6. Species described only as “tropical / subtropical” get 3 tropical representative points (South America, Africa, South-East Asia). Re-introduction sites in brackets don't affect native-range matching.
7. Eight species (polar bear, snowy owl, dog, horse, mule, domestic pigeon, fancy rat, eelgrass) use hand-placed points in `data/locations_manual.json`, each with a Wikipedia source.

Current result: all 1000 species have markers, 2037 points in total, **all `approx: true`**.
- 911 species are matched from range text, 8 use manual points, and 81 only have “widespread” representative points (mostly ocean fish, molds and yeasts, and other globally distributed species).
- 10 species are flagged “location to be verified” (`location_pending: true`). One is the domestication origin of the fancy mouse. The other 9 are cultivated species whose cards give no origin (Chinese hibiscus, rapeseed, sesame, coconut palm, alfalfa, garden strawberry, radish, onion, snow fungus), so they only have widespread representative points.
- The range text on 7 more cards itself contains “待核” (to verify): red kangaroo, red fox, raccoon, pea aphid, black soldier fly, common green lacewing, mayflies.

Every point carries `kind` (how it was placed) and `label`. Every species carries `kingdom`, `category`, `range_note`, `source` (Wikipedia article) and `location_method`. The side panel shows these together with review hints.

## Third-party assets and licences

| Asset | Licence |
|---|---|
| [globe.gl](https://github.com/vasturiano/globe.gl) 2.46 (incl. three-globe) | MIT, see `frontend/vendor/LICENSE-*.txt` |
| [three.js](https://threejs.org/) | MIT |
| Globe textures `earth-blue-marble.jpg`, `earth-topology.png` (from the three-globe examples, derived from NASA Blue Marble / NASA topography) | Public domain (NASA) |
| [Natural Earth](https://www.naturalearthdata.com/) 1:50m country boundaries (used to build `gazetteer_ne.json`) | Public domain |
| FastAPI / Uvicorn | MIT / BSD-3 |

The front end loads nothing from a CDN at runtime; all files are local.
