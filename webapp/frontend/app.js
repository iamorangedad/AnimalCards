/* 动物卡片地球 — 前端（无构建步骤，原生 JS + globe.gl） */
(() => {
"use strict";
const CATS = [
  ["宠物", "#f08a24", "#fdebd8"], ["农场", "#9a6a3a", "#f1e6da"], ["高原草原", "#c9a400", "#faf3cc"], ["森林", "#2e9e5b", "#dcf2e4"],
  ["海洋", "#1f6fd6", "#dceafb"], ["鸟类", "#8e5cd9", "#ece2fa"], ["爬行两栖", "#13a3a3", "#d6f3f3"], ["昆虫", "#e0457b", "#fbe0ea"],
  // 植物（绿色系）
  ["花卉", "#d6409f", "#fbe1f1"], ["树木", "#2f7d32", "#dcefdc"], ["农作物", "#b5892a", "#f6ecd2"], ["水果蔬菜", "#e8572c", "#fde3d9"],
  ["沙漠植物", "#a8733a", "#f3e6d6"], ["水生植物", "#1894b8", "#d5eef6"],
  // 真菌
  ["蘑菇", "#7a4f2f", "#eee2d8"], ["霉菌酵母", "#6a7d3c", "#e6ecd6"]];
const KINGDOMS = [["动物", CATS.slice(0, 8).map(c => c[0])], ["植物", CATS.slice(8, 14).map(c => c[0])], ["真菌", CATS.slice(14).map(c => c[0])]];
const CAT = Object.fromEntries(CATS.map(([n, c, l]) => [n, { c, l }]));
const IUCN = { CR: ["#d81e05", "极危"], EN: ["#fc7f3f", "濒危"], VU: ["#e0a800", "易危"], NT: ["#9aa83b", "近危"], LC: ["#60c659", "无危"],
  DD: ["#6b7075", "数据缺乏"], NE: ["#6b7075", "未评估/家养/栽培"], EX: ["#000", "灭绝"], EW: ["#542344", "野外灭绝"] };
const $ = s => document.querySelector(s);
const state = { animals: [], byId: {}, cats: new Set(CATS.map(c => c[0])), iucn: new Set(), alt: 2.4, markers: [], rotate: true, idleTimer: null };
let world;

const enc = p => p.split("/").map(encodeURIComponent).join("/");
function urls(a) {
  if (a.card_png_url) return a;
  const PRE = { "动物": "cards/", "植物": "plants/", "真菌": "fungi/" };  // 与后端 /cards /plants /fungi 对应
  const u = p => { const [k, ...rest] = p.split("/"); return (PRE[k] || "cards/") + enc(PRE[k] ? rest.join("/") : p); };
  return Object.assign(a, { card_png_url: u(a.card_png), card_pdf_url: u(a.card_pdf), thumb_url: a.thumb, avatar_url: a.avatar });
}
async function load() {
  try {
    const r = await fetch("api/animals?limit=1000");
    if (!r.ok) throw new Error(r.status);
    const j = await r.json(); return j.items;
  } catch (e) {  // 纯静态部署时的后备
    const j = await (await fetch("data/animals.json")).json(); return j.animals;
  }
}

/* ---------- 标注：同点错开 + 按缩放聚合 ---------- */
function buildMarkers() {
  const list = [];
  for (const a of state.animals) {
    if (!state.cats.has(a.category) || !state.iucn.has(a.iucn)) continue;
    a.locations.forEach((l, i) => list.push({ a, l, i, lat: l.lat, lng: l.lon }));
  }
  const groups = {};
  for (const m of list) (groups[m.lat.toFixed(1) + "," + m.lng.toFixed(1)] ||= []).push(m);
  for (const g of Object.values(groups)) {
    if (g.length < 2) continue;
    g.sort((x, y) => x.a.number - y.a.number);
    g.forEach((m, k) => {   // 螺旋错开，避免完全重叠（仅为显示）
      const ring = Math.floor(Math.sqrt(k)), ang = k * 2.39996, r = 0.55 + 0.55 * Math.sqrt(k);
      m.lat = m.l.lat + r * Math.sin(ang);
      m.lng = m.l.lon + r * Math.cos(ang) / Math.max(0.25, Math.cos(m.l.lat * Math.PI / 180));
      m.jitter = true; void ring;
    });
  }
  state.markers = list;
  $("#shown").textContent = `显示 ${new Set(list.map(m => m.a.id)).size} 种 · ${list.length} 个标注`;
}
function cellFor(alt) { return alt < 0.32 ? 0 : Math.min(16, alt * 5.2); }
function cluster() {
  const cell = cellFor(state.alt), out = [];
  if (!cell) return state.markers.map(m => ({ single: m, lat: m.lat, lng: m.lng }));
  const cl = [];
  for (const m of state.markers) {
    let best = null, bd = Infinity;
    for (const c of cl) {
      let dl = Math.abs(c.lng - m.lng); if (dl > 180) dl = 360 - dl;
      const d = Math.hypot(c.lat - m.lat, dl * Math.cos(m.lat * Math.PI / 180));
      if (d < cell && d < bd) { bd = d; best = c; }
    }
    if (best) { best.items.push(m); const n = best.items.length; best.lat += (m.lat - best.lat) / n; best.lng += (m.lng - best.lng) / n; }
    else cl.push({ lat: m.lat, lng: m.lng, items: [m] });
  }
  for (const c of cl) out.push(c.items.length === 1 ? { single: c.items[0], lat: c.items[0].lat, lng: c.items[0].lng } : c);
  return out;
}
function markerEl(m) {
  const el = document.createElement("div"); const a = m.a;
  el.className = "mk"; el.style.setProperty("--c", CAT[a.category].c);
  el.style.backgroundImage = `url("${a.avatar_url}")`;
  el.setAttribute("role", "button"); el.setAttribute("aria-label", a.name_zh);
  el.addEventListener("mouseenter", ev => tip(ev, `<b>${a.name_zh}</b> <small>${a.name_en}</small><br><small>${m.l.label}${m.l.approx ? "（近似）" : ""}</small>`));
  el.addEventListener("mousemove", moveTip); el.addEventListener("mouseleave", hideTip);
  el.addEventListener("click", ev => { ev.stopPropagation(); hideTip(); openAnimal(a, m.l); });
  return el;
}
function clusterEl(c) {
  const el = document.createElement("div"); el.className = "cl";
  const cats = {}; c.items.forEach(m => cats[m.a.category] = (cats[m.a.category] || 0) + 1);
  const top = Object.entries(cats).sort((x, y) => y[1] - x[1]).slice(0, 3);
  el.innerHTML = top.map(([k]) => `<span class="ring" style="background:${CAT[k].c}"></span>`).join("") + `<span>${c.items.length}</span>`;
  const names = [...new Set(c.items.map(m => m.a.name_zh))];
  el.addEventListener("mouseenter", ev => tip(ev, `<b>${names.length} 种</b><br><small>${names.slice(0, 6).join("、")}${names.length > 6 ? "…" : ""}</small>`));
  el.addEventListener("mousemove", moveTip); el.addEventListener("mouseleave", hideTip);
  el.addEventListener("click", ev => {
    ev.stopPropagation(); hideTip();
    if (state.alt < 0.55) openList(c);
    else { stopRotate(); world.pointOfView({ lat: c.lat, lng: c.lng, altitude: Math.max(0.25, state.alt * 0.42) }, 900); }
  });
  return el;
}
let rcTimer = null;
function render() {
  const data = cluster();
  world.htmlElementsData(data);
}
function scheduleRender() { clearTimeout(rcTimer); rcTimer = setTimeout(render, 120); }

/* ---------- 提示框 ---------- */
const tipEl = () => $("#tooltip");
function tip(ev, html) { const t = tipEl(); t.innerHTML = html; t.hidden = false; moveTip(ev); }
function moveTip(ev) { const t = tipEl(); t.style.left = ev.clientX + "px"; t.style.top = ev.clientY + "px"; }
function hideTip() { tipEl().hidden = true; }

/* ---------- 面板 ---------- */
const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
function openPanel(html) { $("#panelBody").innerHTML = html; $("#panel").hidden = false; $("#panel").scrollTop = 0; stopRotate(); }
function closePanel() { $("#panel").hidden = true; if (location.hash) history.replaceState(null, "", location.pathname + location.search); scheduleResume(); }
function openAnimal(a, loc) {
  const c = CAT[a.category], iu = IUCN[a.iucn] || ["#6b7075", a.iucn];
  const review = [];
  if (a.location_method === "wide") review.push("广泛分布：只放了代表点");
  if (a.location_method === "manual") review.push("位置为人工补充（见来源）");
  if (a.location_pending) review.push("位置待核");
  if (/待核/.test(a.range_text)) review.push("分布文字含待核");
  if (a.domestic) review.push("家养动物：标注为原产/驯化起源地");
  if (a.cultivated) review.push("栽培种：标注为原产地/起源地，不是全部种植区");
  openPanel(`
    <div class="p-head"><span class="p-no">No.${String(a.number).padStart(3, "0")}</span>
      <span class="p-cat" style="--c:${c.c};--cl:${c.l}">${esc(a.category)}</span></div>
    <div class="p-name">${esc(a.name_zh)}</div>
    <div class="p-en">${esc(a.name_en)} · <i>${esc(a.latin)}</i></div>
    <div class="p-wrap">
      <div class="p-card" id="pCard" title="点击查看高清卡片"><img src="${a.thumb_url}" alt="${esc(a.name_zh)} 卡片" loading="eager"></div>
      <div class="facts">
        <div class="f"><span class="k">IUCN</span><span><span class="iucn" style="background:${iu[0]}">${esc(a.iucn)}</span>${esc(iu[1])}<br><small>${esc(a.iucn_note)}</small></span></div>
        <div class="f"><span class="k">分布</span><span>${esc(a.range_text)}</span></div>
        <div class="f"><span class="k">标注</span><ul class="locs">${a.locations.map(l => `<li>📍 ${esc(l.label)}${l.approx ? '<span class="ap">近似</span>' : ""}</li>`).join("")}</ul></div>
        <div class="f"><span class="k">说明</span><span>${esc(a.range_note)}<br>${review.map(r => `<span class="badge-review">${esc(r)}</span>`).join("")}</span></div>
        <div class="f"><span class="k">来源</span><span>${a.source ? `<a href="${esc(a.source)}" target="_blank" rel="noopener">${esc(decodeURIComponent(a.source.split("/wiki/")[1] || a.source))}</a>` : "—"}<br><small>${esc((a.sources_card || []).join("；"))}</small></span></div>
      </div>
    </div>
    <div class="p-actions"><a class="pri" href="${a.card_png_url}" target="_blank" rel="noopener">查看高清 PNG</a><a href="${a.card_pdf_url}" download>下载 PDF</a></div>`);
  $("#pCard").addEventListener("click", () => { $("#lbImg").src = a.card_png_url; $("#lbImg").alt = a.name_zh; $("#lightbox").hidden = false; });
  history.replaceState(null, "", "#a=" + encodeURIComponent(a.id));
  void loc;
}
function openList(c) {
  const seen = new Set(), items = c.items.filter(m => !seen.has(m.a.id) && seen.add(m.a.id));
  openPanel(`<div class="p-list"><h3>这里有 ${items.length} 种</h3>${items.map(m => `
    <div class="item" data-id="${m.a.id}"><img src="${m.a.avatar_url}" style="--c:${CAT[m.a.category].c}" alt="">
    <div><b>${esc(m.a.name_zh)}</b><br><small>${esc(m.a.category)} · ${esc(m.l.label)}</small></div></div>`).join("")}</div>`);
  document.querySelectorAll(".p-list .item").forEach(el => el.addEventListener("click", () => openAnimal(state.byId[el.dataset.id])));
}
function openAbout(ev) {
  ev && ev.preventDefault();
  openPanel(`<h3 style="margin:4px 0 8px">数据与来源</h3><div class="facts" style="padding:8px 10px;line-height:1.7">
   <p>• 卡片内容来自本仓库 1000 张卡片（动物 760、植物 200、真菌 40；维基百科、IUCN 红色名录等，见每张卡的来源脚注）。</p>
   <p>• 标注位置由脚本根据卡片“分布”文字自动匹配：国家用 Natural Earth（公有领域）的国家标注点或按方位推算的国内点；大洲、海域、地理区用人工设定的大致中心点；少数（${state.animals.filter(a => a.location_method === "manual").length} 种）为人工补充并附来源。</p>
   <p>• 所有标注都是<b>近似代表点</b>，不代表精确分布范围；家养动物、栽培植物和栽培食用菌标注的是原产地或起源地；广泛分布的物种只放了几个代表点。</p>
   <p>• 数据由 AI 辅助整理，<b>需人工复核</b>。</p>
   <p>• 地球贴图：NASA Blue Marble（公有领域，取自 three-globe 示例）；3D 引擎：globe.gl / three.js（MIT）。</p></div>`);
}

/* ---------- 筛选 ---------- */
function chips() {
  const cc = {}, ic = {};
  state.animals.forEach(a => { cc[a.category] = (cc[a.category] || 0) + 1; ic[a.iucn] = (ic[a.iucn] || 0) + 1; });
  const chip = ([n, c, l]) => `<button class="chip on" data-cat="${n}" style="--c:${c};--cl:${l}"><span class="dot"></span>${n}<span class="n">${cc[n] || 0}</span></button>`;
  $("#catChips").innerHTML = KINGDOMS.map(([k, cs]) => `<div class="kg"><button class="kchip" data-kingdom="${k}" title="点击：只看${k}；再点：全部显示">${k}<span class="n">${cs.reduce((s, n) => s + (cc[n] || 0), 0)}</span></button>${CATS.filter(c => cs.includes(c[0])).map(chip).join("")}</div>`).join("");
  document.querySelectorAll(".kchip").forEach(b => b.addEventListener("click", () => {
    const cs = KINGDOMS.find(k => k[0] === b.dataset.kingdom)[1];
    const only = cs.every(n => state.cats.has(n)) && state.cats.size === cs.length;
    state.cats.clear(); (only ? CATS.map(c => c[0]) : cs).forEach(n => state.cats.add(n));
    syncChips(); buildMarkers(); render();
  }));
  const codes = Object.keys(IUCN).filter(k => ic[k]);
  codes.forEach(k => state.iucn.add(k));
  $("#iucnChips").innerHTML = codes.map(k => `<button class="chip on" data-iucn="${k}" style="--c:${IUCN[k][0]};--cl:#fff" title="${IUCN[k][1]}"><span class="dot"></span>${k}<span class="n">${ic[k]}</span></button>`).join("");
  document.querySelectorAll(".chip").forEach(b => b.addEventListener("click", ev => {
    const set = b.dataset.cat ? state.cats : state.iucn, key = b.dataset.cat || b.dataset.iucn;
    const group = b.dataset.cat ? "#catChips" : "#iucnChips";
    if (ev.shiftKey || ev.altKey) {  // 只看这一类
      set.clear(); set.add(key);
      document.querySelectorAll(group + " .chip").forEach(x => x.classList.toggle("on", x === b) || x.classList.toggle("off", x !== b));
    } else if (set.has(key)) set.delete(key); else set.add(key);
    syncChips(); buildMarkers(); render();
  }));
}
function syncChips() {
  document.querySelectorAll("#catChips .chip").forEach(x => { const on = state.cats.has(x.dataset.cat); x.classList.toggle("on", on); x.classList.toggle("off", !on); });
  document.querySelectorAll("#iucnChips .chip").forEach(x => { const on = state.iucn.has(x.dataset.iucn); x.classList.toggle("on", on); x.classList.toggle("off", !on); });
}
function reset() {
  CATS.forEach(c => state.cats.add(c[0])); document.querySelectorAll("#iucnChips .chip").forEach(x => state.iucn.add(x.dataset.iucn));
  syncChips(); buildMarkers(); render(); world.pointOfView({ altitude: 2.4 }, 800);
}

/* ---------- 搜索 ---------- */
function norm(s) { return (s || "").toLowerCase().replace(/\s+/g, ""); }
function searchSetup() {
  const q = $("#q"), ul = $("#suggest"); let items = [], act = 0;
  const show = () => {
    const t = norm(q.value); if (!t) { ul.hidden = true; return; }
    items = state.animals.filter(a => [a.name_zh, a.name_en, a.latin, a.id].some(x => norm(x).includes(t)))
      .sort((x, y) => (norm(x.name_zh).startsWith(t) ? 0 : 1) - (norm(y.name_zh).startsWith(t) ? 0 : 1) || x.number - y.number).slice(0, 12);
    act = 0;
    ul.innerHTML = items.length ? items.map((a, i) => `<li data-i="${i}" class="${i ? "" : "active"}" role="option"><img src="${a.avatar_url}" style="--c:${CAT[a.category].c}" alt="">
      <div><div class="nm">${esc(a.name_zh)}</div><div class="en">${esc(a.name_en)}</div></div><span class="no">${a.category} · ${String(a.number).padStart(3, "0")}</span></li>`).join("")
      : `<li>没有找到 “${esc(q.value)}”</li>`;
    ul.hidden = false;
    ul.querySelectorAll("li[data-i]").forEach(li => li.addEventListener("mousedown", e => { e.preventDefault(); pick(items[+li.dataset.i]); }));
  };
  const pick = a => { if (!a) return; ul.hidden = true; q.value = a.name_zh; q.blur(); flyTo(a); };
  q.addEventListener("input", show); q.addEventListener("focus", show);
  q.addEventListener("blur", () => setTimeout(() => ul.hidden = true, 150));
  q.addEventListener("keydown", e => {
    const lis = ul.querySelectorAll("li[data-i]");
    if (e.key === "ArrowDown" || e.key === "ArrowUp") { e.preventDefault(); act = (act + (e.key === "ArrowDown" ? 1 : lis.length - 1)) % Math.max(1, lis.length); lis.forEach((l, i) => l.classList.toggle("active", i === act)); }
    if (e.key === "Enter") pick(items[act]);
    if (e.key === "Escape") { ul.hidden = true; q.blur(); }
  });
}
function flyTo(a) {
  if (!state.cats.has(a.category) || !state.iucn.has(a.iucn)) { state.cats.add(a.category); state.iucn.add(a.iucn); syncChips(); buildMarkers(); }
  const l = a.locations[0];
  stopRotate();
  if (l) world.pointOfView({ lat: l.lat, lng: l.lon, altitude: 0.9 }, 1400);
  openAnimal(a, l);
  setTimeout(render, 1450);
}

/* ---------- 自动旋转 ---------- */
function stopRotate() { world.controls().autoRotate = false; clearTimeout(state.idleTimer); }
function scheduleResume() {
  clearTimeout(state.idleTimer);
  state.idleTimer = setTimeout(() => { if (state.rotate && $("#panel").hidden) world.controls().autoRotate = true; }, 15000);
}

/* ---------- 启动 ---------- */
async function main() {
  const list = await load();
  state.animals = list.map(urls).sort((x, y) => x.number - y.number);
  state.byId = Object.fromEntries(state.animals.map(a => [a.id, a]));
  $("#countAll").textContent = state.animals.length;
  chips(); buildMarkers();
  const el = $("#globe");
  world = Globe({ animateIn: true })(el)
    .globeImageUrl("img/earth-blue-marble.jpg").bumpImageUrl("img/earth-topology.png")
    .backgroundColor("rgba(0,0,0,0)").showAtmosphere(true).atmosphereColor("#8cc4ff").atmosphereAltitude(0.18)
    .htmlElementsData([]).htmlLat(d => d.lat).htmlLng(d => d.lng).htmlAltitude(0.01)
    .htmlElement(d => d.single ? markerEl(d.single) : clusterEl(d))
    .onZoom(pov => { const changed = Math.abs(pov.altitude - state.alt) > 0.04; state.alt = pov.altitude; if (changed) scheduleRender(); })
    .onGlobeClick(() => { hideTip(); });
  if (world.htmlElementVisibilityModifier) world.htmlElementVisibilityModifier((elx, vis) => { elx.style.opacity = vis ? 1 : 0; elx.style.pointerEvents = vis ? "auto" : "none"; });
  const fit = () => world.width(el.clientWidth).height(el.clientHeight);
  fit(); window.addEventListener("resize", fit);
  world.pointOfView({ lat: 25, lng: 105, altitude: 2.4 });
  const ctr = world.controls(); ctr.autoRotate = true; ctr.autoRotateSpeed = 0.45; ctr.minDistance = 112; ctr.maxDistance = 900;
  ctr.addEventListener("start", () => { stopRotate(); });
  ctr.addEventListener("end", scheduleResume);
  render();
  $("#loading").classList.add("done");
  searchSetup();
  $("#panelClose").onclick = closePanel;
  $("#lbClose").onclick = () => $("#lightbox").hidden = true;
  $("#lightbox").addEventListener("click", e => { if (e.target.id === "lightbox") $("#lightbox").hidden = true; });
  $("#resetBtn").onclick = reset;
  $("#aboutLink").onclick = openAbout;
  $("#rotateTog").onchange = e => { state.rotate = e.target.checked; world.controls().autoRotate = state.rotate && $("#panel").hidden; };
  $("#filterToggle").onclick = () => { const f = $("#filters"); f.classList.toggle("open"); $("#filterToggle").setAttribute("aria-expanded", f.classList.contains("open")); };
  document.addEventListener("keydown", e => { if (e.key === "Escape") { $("#lightbox").hidden = true; closePanel(); } });
  const m = location.hash.match(/a=([^&]+)/);
  if (m && state.byId[decodeURIComponent(m[1])]) flyTo(state.byId[decodeURIComponent(m[1])]);
  window.__app = { state, world, flyTo, openList, render };  // 便于测试
}
main().catch(err => { $("#loading").textContent = "加载失败：" + err.message; console.error(err); });
})();
