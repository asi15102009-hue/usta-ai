/* ================= TRANSLATIONS (UI chrome) ================= */
const T = {
  kg: {
    tagline:"Курулуш инженердик эсептөөлөрү",
    projectNameLabel:"Объекттин аты", projectNamePh:"Мис.: Тургун үй, Чүй көч. 14", dateLabel:"Дата",
    modFundament:"Фундамент", modFundamentDesc:"Бетон, цемент, кум, шагыл жана арматура көлөмүн эсептейт.",
    modDubal:"Дубал", modDubalDesc:"Материал санын, раствор/клей жана сеткинин муктаждыгын эсептейт.",
    modChatyr:"Чатыр", modChatyrDesc:"Жабуу материалын, стропиланы, конекти жана изоляцияны эсептейт.",
    back:"Артка", secInputs:"Киргизилүүчү маалыматтар", calcBtn:"Эсептөө", pdfBtn:"PDF жүктөө", resultsReady:"Эсептөө бүттү",
    funType:"Фундаменттин түрү", funTypeLenta:"Ленталык", funTypePlita:"Плиталык", funTypeBagana:"Баганалуу",
    concreteGrade:"Бетон маркасы", lengthLabel:"Узундугу", widthLabel:"Туурасы", heightLabel:"Бийиктиги",
    rebarDiameter:"Арматуранын диаметри", rebarCount:"Арматуранын саны", reservePercent:"Запас пайызы",
    funNote:"Эскертүү: бетон курамынын пропорциялары орточо нормативдик көрсөткүчтөр боюнча эсептелди. Так долбоор үчүн инженер менен текшериңиз.",
    r_concrete_volume_m3:"Бетон", r_cement_kg:"Цемент", r_sand_m3:"Кум", r_gravel_m3:"Шагыл",
    r_rebar_kg:"Арматура", r_opalubka_m2:"Опалубка аянты",
    wallMaterial:"Материал", matKirpich:"Кирпич", matPescoblok:"Пескоблок", matPenoblok:"Пеноблок", matGazoblok:"Газоблок", matShlakoblok:"Шлакоблок",
    seamLabel:"Шов", thicknessLabel:"Калыңдыгы", doorsLabel:"Эшиктердин жалпы аянты", windowsLabel:"Терезелердин жалпы аянты",
    dubalNote:"Эскертүү: материалдын өлчөмдөрү орточо стандарттык көрсөткүчтөр боюнча алынды. Так каталог өлчөмдөрү боюнча айырмаланышы мүмкүн.",
    r_wall_area_m2:"Дубалдын аянты", r_material_count_pcs:"Материал саны", r_mortar_volume_m3:"Раствор көлөмү",
    r_glue_weight_kg:"Клей салмагы", r_mesh_area_m2:"Сетка аянты",
    roofForm:"Формасы", formOdno:"Однoскатная", formDvux:"Двухскатная", formChetyre:"Четырехскатная", formL:"L-формасы", formG:"Г-формасы", formT:"Т-формасы",
    roofMaterial:"Материал", matMetal:"Металл профиль", matOndulin:"Ондулин", matShifer:"Шифер", matCherepitsa:"Металл черепица",
    buildLength:"Үйдүн узундугу", buildWidth:"Үйдүн туурасы", angleLabel:"Бурч", svesLabel:"Свес",
    chatyrNote:"Эскертүү: чатыр эсептөөлөрү жөнөкөйлөштүрүлгөн геометрия менен алынды. Татаал чатыр формалары үчүн инженер менен текшериңиз.",
    r_total_area_m2:"Жалпы аянты", r_covering_material_m2:"Жабуу материалы", r_reyka_m:"Рейка", r_stropila_count:"Стропила саны",
    r_stropila_length_m:"Стропила узундугу", r_konek_m:"Конек", r_zhelob_m:"Желоб", r_gidro_m2:"Гидроизоляция", r_paro_m2:"Пароизоляция",
    footer:"УСТА АИ · v0.1 (Guest режими, каттоосуз) · Бардык эсептөөлөр орточо нормативдик маалыматтарга негизделген",
    errRequired:"Бул талаа бош болбошу керек.", errPositive:"Маани 0дөн чоң болушу керек.", errFormat:"Туура эмес формат.",
    errNetwork:"Backend менен байланыш жок. Сервер иштеп жатабы текшериңиз (python app.py).",
    unitsShort:{m:"м", m2:"м²", m3:"м³", kg:"кг", mm:"мм", pcs:"даана", pct:"%", deg:"°"}
  },
  ru: {
    tagline:"Инженерные строительные расчёты",
    projectNameLabel:"Название объекта", projectNamePh:"Напр.: Жилой дом, ул. Чуй 14", dateLabel:"Дата",
    modFundament:"Фундамент", modFundamentDesc:"Рассчитывает объём бетона, цемента, песка, щебня и арматуры.",
    modDubal:"Стена", modDubalDesc:"Рассчитывает количество материала, раствор/клей и сетку.",
    modChatyr:"Крыша", modChatyrDesc:"Рассчитывает кровельный материал, стропила, конёк и изоляцию.",
    back:"Назад", secInputs:"Исходные данные", calcBtn:"Рассчитать", pdfBtn:"Скачать PDF", resultsReady:"Расчёт готов",
    funType:"Тип фундамента", funTypeLenta:"Ленточный", funTypePlita:"Плитный", funTypeBagana:"Столбчатый",
    concreteGrade:"Марка бетона", lengthLabel:"Длина", widthLabel:"Ширина", heightLabel:"Высота",
    rebarDiameter:"Диаметр арматуры", rebarCount:"Количество арматуры", reservePercent:"Процент запаса",
    funNote:"Примечание: пропорции бетонной смеси рассчитаны по усреднённым нормативным данным. Для точного проекта проконсультируйтесь с инженером.",
    r_concrete_volume_m3:"Бетон", r_cement_kg:"Цемент", r_sand_m3:"Песок", r_gravel_m3:"Щебень",
    r_rebar_kg:"Арматура", r_opalubka_m2:"Площадь опалубки",
    wallMaterial:"Материал", matKirpich:"Кирпич", matPescoblok:"Пескоблок", matPenoblok:"Пеноблок", matGazoblok:"Газоблок", matShlakoblok:"Шлакоблок",
    seamLabel:"Шов", thicknessLabel:"Толщина", doorsLabel:"Общая площадь дверей", windowsLabel:"Общая площадь окон",
    dubalNote:"Примечание: размеры материалов взяты по усреднённым стандартным значениям. Могут отличаться от каталожных.",
    r_wall_area_m2:"Площадь стены", r_material_count_pcs:"Кол-во материала", r_mortar_volume_m3:"Объём раствора",
    r_glue_weight_kg:"Вес клея", r_mesh_area_m2:"Площадь сетки",
    roofForm:"Форма", formOdno:"Односкатная", formDvux:"Двухскатная", formChetyre:"Четырёхскатная", formL:"L-образная", formG:"Г-образная", formT:"Т-образная",
    roofMaterial:"Материал", matMetal:"Металлопрофиль", matOndulin:"Ондулин", matShifer:"Шифер", matCherepitsa:"Металлочерепица",
    buildLength:"Длина здания", buildWidth:"Ширина здания", angleLabel:"Угол", svesLabel:"Свес",
    chatyrNote:"Примечание: расчёт кровли выполнен по упрощённой геометрии. Для сложных форм крыши проконсультируйтесь с инженером.",
    r_total_area_m2:"Общая площадь", r_covering_material_m2:"Кровельный материал", r_reyka_m:"Рейка", r_stropila_count:"Кол-во стропил",
    r_stropila_length_m:"Длина стропил", r_konek_m:"Конёк", r_zhelob_m:"Жёлоб", r_gidro_m2:"Гидроизоляция", r_paro_m2:"Пароизоляция",
    footer:"УСТА АИ · v0.1 (Гостевой режим, без регистрации) · Все расчёты основаны на усреднённых нормативных данных",
    errRequired:"Поле не должно быть пустым.", errPositive:"Значение должно быть больше 0.", errFormat:"Неверный формат.",
    errNetwork:"Нет связи с backend. Проверьте, запущен ли сервер (python app.py).",
    unitsShort:{m:"м", m2:"м²", m3:"м³", kg:"кг", mm:"мм", pcs:"шт", pct:"%", deg:"°"}
  }
};

let lang = 'kg';
const lastInputs = {}; // uiModule -> raw form data sent to the API (reused for PDF export)

/* map UI module name -> backend API module name, and its field ids -> API field names */
const MODULE_MAP = {
  fundament: {
    api: 'foundation',
    fields: {
      type: 'f_type', grade: 'f_grade', length: 'f_length', width: 'f_width', height: 'f_height',
      rebar_diameter: 'f_rdia', rebar_count: 'f_rcount', reserve: 'f_reserve'
    }
  },
  dubal: {
    api: 'wall',
    fields: {
      material: 'w_material', seam: 'w_seam', length: 'w_length', height: 'w_height',
      thickness: 'w_thickness', doors: 'w_doors', windows: 'w_windows', reserve: 'w_reserve'
    }
  },
  chatyr: {
    api: 'roof',
    fields: {
      form: 'r_form', material: 'r_material', length: 'r_length', width: 'r_width',
      angle: 'r_angle', sves: 'r_sves'
    }
  }
};

function setLang(l){
  lang = l;
  document.getElementById('btn-kg').classList.toggle('active', l==='kg');
  document.getElementById('btn-ru').classList.toggle('active', l==='ru');
  applyTranslations();
}
function applyTranslations(){
  document.querySelectorAll('[data-t]').forEach(el=>{
    const key = el.getAttribute('data-t');
    if(T[lang][key] !== undefined) el.textContent = T[lang][key];
  });
  document.querySelectorAll('[data-tph]').forEach(el=>{
    const key = el.getAttribute('data-tph');
    if(T[lang][key] !== undefined) el.setAttribute('placeholder', T[lang][key]);
  });
}
applyTranslations();
document.getElementById('projectDate').value = new Date().toISOString().slice(0,10);

/* ================= NAVIGATION ================= */
function openModule(name){
  document.getElementById('view-home').style.display = 'none';
  document.getElementById('view-fundament').style.display = name==='fundament' ? 'block':'none';
  document.getElementById('view-dubal').style.display = name==='dubal' ? 'block':'none';
  document.getElementById('view-chatyr').style.display = name==='chatyr' ? 'block':'none';
  window.scrollTo(0,0);
}
function goHome(){
  document.getElementById('view-home').style.display='block';
  document.getElementById('view-fundament').style.display='none';
  document.getElementById('view-dubal').style.display='none';
  document.getElementById('view-chatyr').style.display='none';
  window.scrollTo(0,0);
}

/* ================= CLIENT-SIDE PRE-VALIDATION (UX only; server is authoritative) ================= */
function clearErr(uiModule, apiField){
  const wrap = document.querySelector(`#view-${uiModule} [data-field="${apiField}"]`);
  if(!wrap) return;
  wrap.classList.remove('has-err');
  wrap.querySelector('.err-msg').textContent='';
}
function setErr(uiModule, apiField, msg){
  const wrap = document.querySelector(`#view-${uiModule} [data-field="${apiField}"]`);
  if(!wrap) return;
  wrap.classList.add('has-err');
  wrap.querySelector('.err-msg').textContent = msg;
}
function errMsgFor(code){
  if(code === 'required') return T[lang].errRequired;
  if(code === 'positive') return T[lang].errPositive;
  return T[lang].errFormat;
}

function collectFormData(uiModule){
  const map = MODULE_MAP[uiModule].fields;
  const data = {};
  Object.entries(map).forEach(([apiField, elId])=>{
    const el = document.getElementById(elId);
    data[apiField] = el.value;
    clearErr(uiModule, apiField);
  });
  return data;
}

/* ================= CALCULATE (calls backend) ================= */
async function calcModule(uiModule){
  const apiModule = MODULE_MAP[uiModule].api;
  const data = collectFormData(uiModule);
  const pdfBtn = document.getElementById(uiModule+'-pdf-btn');
  const resultsBox = document.getElementById(uiModule+'-results');

  pdfBtn.disabled = true;
  resultsBox.classList.remove('show');

  let resp, json;
  try{
    resp = await fetch(`/api/${apiModule}`, {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify(data)
    });
    json = await resp.json();
  } catch(e){
    alert(T[lang].errNetwork);
    return;
  }

  if(!json.ok){
    if(json.errors){
      Object.entries(json.errors).forEach(([field, code])=>{
        setErr(uiModule, field, errMsgFor(code));
      });
    }
    return;
  }

  renderResults(uiModule, json.data);
  lastInputs[uiModule] = data;
  pdfBtn.disabled = false;
}

/* ================= RENDER RESULTS ================= */
const RESULT_KEYS = {
  fundament: ['concrete_volume_m3','cement_kg','sand_m3','gravel_m3','rebar_kg','opalubka_m2'],
  dubal: ['wall_area_m2','material_count_pcs','mortar_volume_m3','glue_weight_kg','mesh_area_m2'],
  chatyr: ['total_area_m2','covering_material_m2','reyka_m','stropila_count','stropila_length_m','konek_m','zhelob_m','gidro_m2','paro_m2']
};
const UNIT_FOR = {
  concrete_volume_m3:'m3', cement_kg:'kg', sand_m3:'m3', gravel_m3:'m3', rebar_kg:'kg', opalubka_m2:'m2',
  wall_area_m2:'m2', material_count_pcs:'pcs', mortar_volume_m3:'m3', glue_weight_kg:'kg', mesh_area_m2:'m2',
  total_area_m2:'m2', covering_material_m2:'m2', reyka_m:'m', stropila_count:'pcs', stropila_length_m:'m',
  konek_m:'m', zhelob_m:'m', gidro_m2:'m2', paro_m2:'m2'
};

function renderResults(uiModule, data){
  const grid = document.getElementById(uiModule+'-result-grid');
  grid.innerHTML = '';
  const u = T[lang].unitsShort;
  RESULT_KEYS[uiModule].forEach(key=>{
    if(!(key in data)) return;
    const label = T[lang]['r_'+key] || key;
    const unit = u[UNIT_FOR[key]] || '';
    const div = document.createElement('div');
    div.className = 'result-item';
    div.innerHTML = `<span class="rk">${label}</span><span class="rv">${data[key]} ${unit}</span>`;
    grid.appendChild(div);
  });
  document.getElementById(uiModule+'-results').classList.add('show');
}

/* ================= PDF EXPORT (backend generates the file) ================= */
async function downloadPdf(uiModule){
  const inputs = lastInputs[uiModule];
  if(!inputs) return;
  const apiModule = MODULE_MAP[uiModule].api;
  const projectName = document.getElementById('projectName').value || '';
  const projectDate = document.getElementById('projectDate').value || '';

  let resp;
  try{
    resp = await fetch(`/api/pdf/${apiModule}`, {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({ lang, project_name: projectName, project_date: projectDate, inputs })
    });
  } catch(e){
    alert(T[lang].errNetwork);
    return;
  }
  if(!resp.ok){
    alert(T[lang].errNetwork);
    return;
  }
  const blob = await resp.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `usta_${apiModule}_${projectDate || 'report'}.pdf`;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}