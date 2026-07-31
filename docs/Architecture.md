# Architecture — УСТА АИ v0.1

## Жалпы көрүнүш

```
Frontend (браузер)  <-- HTTP/JSON -->  Backend (Flask, Python)
   index.html                              app.py
   style.css                                 |-- foundation.py
   script.js                                 |-- wall.py
                                              |-- roof.py
                                              |-- pdf.py
                                              |-- labels.py
                                              |-- utils.py
```

Клиент-сервер архитектурасы колдонулду, себеби:
- эсептөө логикасы бир жерде (backend) сакталат — frontend жана келечектеги мобилдик
  тиркеме (NFR-002гө карай) бир API колдоно алат;
- PDF генерациясы серверде жасалат (кыргызча тамгаларды колдогон шрифт менен), бул
  клиенттик китепканаларга көз каранды болбойт;
- валидация эки жерде: клиентте (тез фидбек) жана серверде (бирден-бир чындык булагы).

## Backend (`/backend`)

| Файл | Милдети |
|---|---|
| `app.py` | Flask колдонмо: `/api/<module>` жана `/api/pdf/<module>` эндпоинттери, `frontend/`ди тейлейт |
| `foundation.py` | FR-001 — фундамент эсептөө логикасы |
| `wall.py` | FR-002 — дубал эсептөө логикасы |
| `roof.py` | FR-003 — чатыр эсептөө логикасы |
| `pdf.py` | FR-004 — PDF отчет генерациясы (reportlab, DejaVuSans шрифти) |
| `labels.py` | PDF үчүн эки тилдүү (кыргызча/орусча) энбелгилер |
| `utils.py` | Жалпы валидация (`validate_fields`, `ValidationError`) |

### API контракты

**`POST /api/foundation` | `/api/wall` | `/api/roof`**

Сурам денеси — модулга ылайык талаалар (мисалы, фундамент үчүн `length`, `width`, `height`,
`grade`, `rebar_diameter`, `rebar_count`, `reserve`, `type`).

Жооп (ийгиликтүү):
```json
{ "ok": true, "data": { "concrete_volume_m3": 2.1, "cement_kg": 504.0, ... } }
```

Жооп (валидация катасы, HTTP 422):
```json
{ "ok": false, "errors": { "length": "positive", "width": "required" } }
```

Ката коддору: `required` (бош талаа), `format` (сан эмес), `positive` (терс же нөл).

**`POST /api/pdf/<module>`**

Сурам денеси:
```json
{ "lang": "kg", "project_name": "...", "project_date": "2026-07-30", "inputs": { ... } }
```

Жооп: PDF файлы (`application/pdf`, `Content-Disposition: attachment`).

## Frontend (`/frontend`)

Vanilla HTML/CSS/JS (framework жок — жеңил жана тез ачылат, NFR-003/NFR-001).

- `index.html` — үч модулдун формалары + башкы меню
- `style.css` — "инженердик схема / blueprint" стилиндеги дизайн
- `script.js` — тил которуу, форма валидациясы (UX үчүн), `fetch` менен backend'ге сурам,
  натыйжаларды рендер кылуу, PDF жүктөө

## Assets (`/assets`)

`fonts/DejaVuSans.ttf` жана `DejaVuSans-Bold.ttf` — PDF ичинде кыргызча тамгаларды
(ө, ү, ң) көрсөтүү үчүн зарыл. Стандарттык PDF шрифттери (Helvetica ж.б.) кирилл
тамгаларын колдобойт.

## Кийинки кадамдар (архитектуралык)

- `FR-005` (сактоо) үчүн: SQLite/PostgreSQL + `projects.py` модулу кошулушу мүмкүн.
- `FR-006–008` (авторизация) үчүн: `auth.py` + сессия/JWT механизми.
- NFR-002 (оффлайн иштөө) толук аткарылышы үчүн: frontend'ди PWA кылып, эсептөө
  логикасын JS'ге да дублдоо же локалдык кэш кошуу керек болот.