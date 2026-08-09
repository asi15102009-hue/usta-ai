/* ================= АРХИТЕКТОР МОДУЛУ (MVP) =================
   Бул файл өз алдынча иштейт, script.js'ке такыр тийбейт.
   Бүт UI ушул жерден динамикалык түрдө #view-architect ичине курулат —
   ошондуктан index.html'ге кичине өзгөртүү (1 карточка + 1 бош div + 2 tag)
   гана керек болду. */

const ARCH = {
  page: 1,
  pageSize: 12,
  filters: { q: '', style: '', floors: '', garage: false, terrace: false, balcony: false, pool: false },
  styles: [],
};

const ARCH_T = {
  kg: {
    title: 'Архитектор', back: 'Артка', searchPh: 'Мис.: рустикальный эки кабаттуу үй, гараж менен...',
    searchBtn: 'Издөө', styleAll: 'Бардык стилдер', floorsAll: 'Бардык кабаттар',
    garage: 'Гараж', terrace: 'Террасса', balcony: 'Балкон', pool: 'Бассейн',
    found: (n) => `${n} долбоор табылды`, empty: 'Эч нерсе табылган жок. Издөөнү же фильтрди өзгөртүп көрүңүз.',
    detailsBtn: 'Толук маалымат', backToGrid: '← Каталогго кайтуу',
    area: 'Аянты', floors: 'Кабат саны', rooms: 'Бөлмө саны', bedrooms: 'Уктоочу бөлмө',
    bathrooms: 'Даараткана', windows: 'Терезе', doors: 'Эшик', roofType: 'Чатыр түрү', shape: 'Формасы',
    editableBadge: 'Редакцияланат', referenceBadge: 'Reference гана',
    editableNote: 'Бул долбоордун structured геометриясы бар — 2D план database\'ден түзүлдү.',
    referenceNote: 'Бул долбоор азырынча reference гана (метадата). Редактирлөө үчүн editable модель түзүлүшү керек — толук 2D/3D редактор Phase 2\'де кошулат.',
    prev: '← Мурунку', next: 'Кийинки →', page: (p, total) => `Барак ${p} / ${total}`,
  },
  ru: {
    title: 'Архитектор', back: 'Назад', searchPh: 'Напр.: рустикальный двухэтажный дом с гаражом...',
    searchBtn: 'Найти', styleAll: 'Все стили', floorsAll: 'Все этажи',
    garage: 'Гараж', terrace: 'Терраса', balcony: 'Балкон', pool: 'Бассейн',
    found: (n) => `Найдено проектов: ${n}`, empty: 'Ничего не найдено. Измените поиск или фильтры.',
    detailsBtn: 'Подробнее', backToGrid: '← Вернуться в каталог',
    area: 'Площадь', floors: 'Этажей', rooms: 'Комнат', bedrooms: 'Спален',
    bathrooms: 'Санузлов', windows: 'Окон', doors: 'Дверей', roofType: 'Тип крыши', shape: 'Форма',
    editableBadge: 'Редактируется', referenceBadge: 'Только reference',
    editableNote: 'У этого проекта есть структурированная геометрия — 2D план построен из данных.',
    referenceNote: 'Этот проект пока только reference (метаданные). Для редактирования нужна editable модель — полный 2D/3D редактор появится в Phase 2.',
    prev: '← Пред.', next: 'След. →', page: (p, total) => `Страница ${p} / ${total}`,
  },
};

function archT() {
  return ARCH_T[typeof lang !== 'undefined' ? lang : 'kg'];
}

function archBuildUI() {
  const t = archT();
  const container = document.getElementById('view-architect');
  container.innerHTML = `
    <div class="module-header">
      <button class="back-btn" onclick="archGoHome()">← <span>${t.back}</span></button>
      <div class="module-title">${t.title}</div>
    </div>
    <div class="bracket">
      <span class="bl"></span><span class="br"></span>
      <div class="arch-toolbar">
        <div class="arch-search">
          <input type="text" id="arch-q" placeholder="${t.searchPh}">
        </div>
        <button class="primary" onclick="archSearch()">${t.searchBtn}</button>
      </div>
      <div class="arch-filters">
        <select id="arch-style-select" onchange="archApplyFilters()"><option value="">${t.styleAll}</option></select>
        <select id="arch-floors-select" onchange="archApplyFilters()">
          <option value="">${t.floorsAll}</option>
          <option value="1">1</option><option value="2">2</option><option value="3">3</option>
        </select>
        <span class="arch-chip" id="chip-garage" onclick="archToggleChip('garage')">${t.garage}</span>
        <span class="arch-chip" id="chip-terrace" onclick="archToggleChip('terrace')">${t.terrace}</span>
        <span class="arch-chip" id="chip-balcony" onclick="archToggleChip('balcony')">${t.balcony}</span>
        <span class="arch-chip" id="chip-pool" onclick="archToggleChip('pool')">${t.pool}</span>
      </div>
      <div class="arch-meta-row" id="arch-meta"></div>
      <div class="arch-grid" id="arch-grid"></div>
      <div class="arch-toolbar" style="margin-top:16px;justify-content:center;">
        <button class="secondary" onclick="archPrevPage()">${t.prev}</button>
        <span class="arch-meta-row" id="arch-page-label" style="margin:0;align-self:center;"></span>
        <button class="secondary" onclick="archNextPage()">${t.next}</button>
      </div>
    </div>
    <div class="bracket" id="arch-detail" style="display:none;margin-top:18px;">
      <span class="bl"></span><span class="br"></span>
      <button class="back-btn" onclick="archCloseDetail()" style="margin-bottom:14px;">${t.backToGrid}</button>
      <div id="arch-detail-content"></div>
    </div>
  `;
}

function archOpen() {
  document.getElementById('view-home').style.display = 'none';
  ['view-fundament', 'view-dubal', 'view-chatyr'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.style.display = 'none';
  });
  const view = document.getElementById('view-architect');
  view.style.display = 'block';
  if (!view.dataset.built) {
    archBuildUI();
    view.dataset.built = '1';
    archLoadStyles();
    archSearch();
  }
  window.scrollTo(0, 0);
}
window.openArchitect = archOpen;

function archGoHome() {
  document.getElementById('view-architect').style.display = 'none';
  if (typeof goHome === 'function') { goHome(); }
  else { document.getElementById('view-home').style.display = 'block'; }
}
window.archGoHome = archGoHome;

async function archLoadStyles() {
  try {
    const resp = await fetch('/api/architect/styles');
    const json = await resp.json();
    if (!json.ok) return;
    ARCH.styles = json.data;
    const select = document.getElementById('arch-style-select');
    json.data.forEach(s => {
      const opt = document.createElement('option');
      opt.value = s.style;
      opt.textContent = `${s.style} (${s.count})`;
      select.appendChild(opt);
    });
  } catch (e) { /* styles are a nice-to-have; silently skip on failure */ }
}

function archToggleChip(feature) {
  ARCH.filters[feature] = !ARCH.filters[feature];
  document.getElementById('chip-' + feature).classList.toggle('active', ARCH.filters[feature]);
  archApplyFilters();
}

function archApplyFilters() {
  ARCH.filters.style = document.getElementById('arch-style-select').value;
  ARCH.filters.floors = document.getElementById('arch-floors-select').value;
  ARCH.page = 1;
  archFetchAndRender();
}

function archSearch() {
  ARCH.filters.q = document.getElementById('arch-q').value.trim();
  ARCH.page = 1;
  archFetchAndRender();
}

function archPrevPage() { if (ARCH.page > 1) { ARCH.page--; archFetchAndRender(); } }
function archNextPage() { ARCH.page++; archFetchAndRender(); }

async function archFetchAndRender() {
  const t = archT();
  const params = new URLSearchParams();
  if (ARCH.filters.q) params.set('q', ARCH.filters.q);
  if (ARCH.filters.style) params.set('style', ARCH.filters.style);
  if (ARCH.filters.floors) params.set('floors', ARCH.filters.floors);
  ['garage', 'terrace', 'balcony', 'pool'].forEach(f => {
    if (ARCH.filters[f]) params.set(f, 'true');
  });
  params.set('page', ARCH.page);
  params.set('page_size', ARCH.pageSize);

  let json;
  try {
    const resp = await fetch('/api/architect/projects?' + params.toString());
    json = await resp.json();
  } catch (e) {
    document.getElementById('arch-grid').innerHTML = `<div class="arch-empty">Backend менен байланыш жок.</div>`;
    return;
  }
  if (!json.ok) return;

  const { projects, total } = json.data;
  document.getElementById('arch-meta').textContent = t.found(total);
  const totalPages = Math.max(1, Math.ceil(total / ARCH.pageSize));
  document.getElementById('arch-page-label').textContent = t.page(ARCH.page, totalPages);

  const grid = document.getElementById('arch-grid');
  if (projects.length === 0) {
    grid.innerHTML = `<div class="arch-empty">${t.empty}</div>`;
    return;
  }
  grid.innerHTML = projects.map(p => archCardHtml(p)).join('');
}

function archThumbSvg(p) {
  /* Чыныгы сүрөт жок — так метаданын өзүнөн жасалган жөнөкөй blueprint иконка (жасалма сүрөт эмес, схема). */
  return `<svg viewBox="0 0 100 70"><polygon points="50,8 92,32 92,62 8,62 8,32" fill="none" stroke="#2B4B63" stroke-width="2"/><line x1="8" y1="32" x2="92" y2="32" stroke="#C4441A" stroke-width="1.5"/></svg>`;
}

function archCardHtml(p) {
  const t = archT();
  const badge = p.project_type === 'editable'
    ? `<span class="arch-badge editable">${t.editableBadge}</span>`
    : `<span class="arch-badge reference">${t.referenceBadge}</span>`;
  return `
    <div class="arch-card" onclick="archOpenDetail(${p.id})">
      <div class="arch-thumb">${archThumbSvg(p)}</div>
      <div class="arch-body">
        <h4>${archEsc(p.title)}</h4>
        <div class="arch-style">${archEsc(p.style || '')}</div>
        <div class="arch-stats">
          <span>${p.area} м²</span><span>${p.floors} ${t.floors.toLowerCase()}</span><span>${p.rooms} ${t.rooms.toLowerCase()}</span>
        </div>
        ${badge}
      </div>
    </div>`;
}

function archEsc(s) {
  const d = document.createElement('div');
  d.textContent = s || '';
  return d.innerHTML;
}

async function archOpenDetail(id) {
  let json;
  try {
    const resp = await fetch('/api/architect/projects/' + id);
    json = await resp.json();
  } catch (e) { return; }
  if (!json.ok) return;
  archRenderDetail(json.data);
  document.getElementById('arch-detail').style.display = 'block';
  document.getElementById('arch-detail').scrollIntoView({ behavior: 'smooth' });
}

function archCloseDetail() {
  document.getElementById('arch-detail').style.display = 'none';
}
window.archOpenDetail = archOpenDetail;
window.archCloseDetail = archCloseDetail;

function archPlanSvg(geometry) {
  if (!geometry || !geometry.floors || !geometry.floors.length) return '';
  const rooms = geometry.floors[0].rooms || [];
  if (!rooms.length) return '';
  const maxX = Math.max(...rooms.map(r => r.x + r.w));
  const maxY = Math.max(...rooms.map(r => r.y + r.h));
  const scale = 40;
  const pad = 20;
  const w = maxX * scale + pad * 2;
  const h = maxY * scale + pad * 2;
  const rects = rooms.map(r => {
    const x = r.x * scale + pad, y = r.y * scale + pad, rw = r.w * scale, rh = r.h * scale;
    return `<rect x="${x}" y="${y}" width="${rw}" height="${rh}" fill="none" stroke="#2B4B63" stroke-width="2"/>
      <text x="${x + rw / 2}" y="${y + rh / 2}" text-anchor="middle" font-family="IBM Plex Sans" font-size="11" fill="#16202B">${archEsc(r.name)}</text>
      <text x="${x + rw / 2}" y="${y + rh / 2 + 14}" text-anchor="middle" font-family="IBM Plex Mono" font-size="9" fill="#4C5A66">${(r.w * r.h).toFixed(1)} м²</text>`;
  }).join('');
  return `<svg viewBox="0 0 ${w} ${h}">${rects}</svg>`;
}

function archRenderDetail(p) {
  const t = archT();
  const isEditable = p.project_type === 'editable';
  const planSvg = isEditable ? archPlanSvg(p.geometry) : '';
  document.getElementById('arch-detail-content').innerHTML = `
    <div class="arch-detail-grid">
      <div class="arch-plan-box">
        ${planSvg || `<div class="arch-empty">${archThumbSvg(p)}</div>`}
        <div class="arch-note ${isEditable ? 'info' : 'warn'}">${isEditable ? t.editableNote : t.referenceNote}</div>
      </div>
      <div class="arch-info-box">
        <h3 style="font-family:'Oswald',sans-serif;text-transform:uppercase;margin-top:0;">${archEsc(p.title)}</h3>
        <p style="color:#4C5A66;font-size:13.5px;">${archEsc(p.description)}</p>
        ${archInfoRow(t.area, p.area + ' м²')}
        ${archInfoRow(t.floors, p.floors)}
        ${archInfoRow(t.rooms, p.rooms)}
        ${archInfoRow(t.bedrooms, p.bedrooms)}
        ${archInfoRow(t.bathrooms, p.bathrooms)}
        ${archInfoRow(t.windows, p.windows)}
        ${archInfoRow(t.doors, p.doors)}
        ${archInfoRow(t.roofType, p.roof_type)}
        ${archInfoRow(t.shape, p.shape)}
        ${archInfoRow(t.garage, p.garage ? '✓' : '—')}
        ${archInfoRow(t.terrace, p.terrace ? '✓' : '—')}
        ${archInfoRow(t.balcony, p.balcony ? '✓' : '—')}
        ${archInfoRow(t.pool, p.pool ? '✓' : '—')}
      </div>
    </div>`;
}

function archInfoRow(k, v) {
  return `<div class="arch-info-row"><span class="k">${archEsc(String(k))}</span><span class="v">${archEsc(String(v))}</span></div>`;
}