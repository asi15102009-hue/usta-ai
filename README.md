# Git сабактары — УСТА АИ долбоору үчүн

Бул кыскача колдонмо долбоор менен иштөө учурунда Git'тин негизги командаларын эстетүү үчүн.

## 1. Долбоорду баштоо

```bash
cd usta-ai
git init
git add .
git commit -m "v0.1: fundament, dubal, chatyr модулдары + PDF"
```

## 2. Учурдагы абалды көрүү

```bash
git status      # кайсы файлдар өзгөргөн
git diff        # эмне өзгөргөнүн көрсөтөт
git log --oneline   # commit тарыхы
```

## 3. Бутактар (branches)

Жаңы модуль үстүндө иштегенде негизги коддон бөлүнүп алуу жакшы практика:

```bash
git checkout -b feature/lestnitsa    # жаңы бутак түзүү жана ага өтүү
# ... код жаз ...
git add .
git commit -m "feat: лестница модулун кошуу (v0.4)"
git checkout main
git merge feature/lestnitsa
```

## 4. Өзгөрүүлөрдү кайра алуу

```bash
git restore <файл>          # commit кылынбаган өзгөрүүлөрдү жокко чыгаруу
git reset --soft HEAD~1     # акыркы commit'ти жокко чыгаруу (файлдар сакталат)
```

## 5. Алыскы репозиторий (мисалы, GitHub)

```bash
git remote add origin https://github.com/<колдонуучу>/usta-ai.git
git push -u origin main
```

Кийинки жолу жөн эле:
```bash
git push
```

## 6. Пайдалуу эрежелер

- Ар бир commit — бир маанилүү өзгөртүү (баары бирге эмес).
- Commit билдирүүсү англисче же кыргызча болсун, бирок так жана кыска
  (мис.: `fix: фундамент эсептөөсүндөгү арматура формуласын оңдоо`).
- `venv/`, `__pycache__/`, `*.pyc` сыяктуу файлдарды `.gitignore`ге кош.

## 7. Бул долбоор үчүн мисал `.gitignore`

venv/
pycache/
*.pyc
.DS_Store
*.pdf


(PDF отчетторду репозиторийге кошпогон жакшы — алар ар бир колдонуучу үчүн динамикалык түзүлөт.)