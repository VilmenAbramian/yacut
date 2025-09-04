# ✂️ YaCut — Укорачиватель ссылок

## 📖 Описание проекта
**YaCut** — это сервис для сокращения длинных ссылок.
🔑 Основные возможности:
- Генерация коротких ссылок и их привязка к исходным URL.
- Автоматическая переадресация по короткой ссылке на оригинальный адрес.

🖥 Интерфейс:
Одна страница с формой, где:
- поле для длинной ссылки (**обязательное**);
- поле для пользовательского варианта короткой ссылки (**необязательное**, до 16 символов).

## 📂 Структура проекта
```
yacut:
  ├── tests
  ├── venv
  ├── yacut
       ├── __pycache__
       ├── static
       ├── templates
       ├── __init__.py
       ├── api_views.py
       ├── error_handlers.py
       ├── forms.py
       ├── models.py
       └── yacut.py
  ├── .env
  ├── .gitignore
  ├── openapi.yml
  ├── pytest.ini
  ├── README.md
  ├── requirements.txt
  └── settings.py
```

## Заполнение конфигурационного .env файла
```
FLASK_APP=yacut
FLASK_DEBUG=1
DATABASE_URI=ChooseDataBase
SECRET_KEY=Your!$ecretKey8

Example:
DATABASE_URI=sqlite:///db.sqlite3
```

## 🚀 Запуск проекта
1. Клонировать репозиторий:
```bash
git clone https://github.com/VilmenAbramian/yacut.git
```
2. Создать и активировать виртуальное окружение:
```bash
python3 -m venv venv
```
Для Linux/macOS:
```bash
source venv/bin/activate
```
Для Windows:
```
venv\Scripts\activate.bat
```
3. Обновить pip и установить зависимости из ```requirements.txt```
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Создать и заполнить файл **.env** в соответствии с [рекомендациями](#заполнение-конфигурационного-env-файла):
```bash
touch .env
```
5. Выполнить миграции:
```bash
flask db init
flask db migrate -m "Имя миграции"
flask db upgrade
```
6. Запустить проект:
```bash
flask run
```
После запуска проект будет доступен по адресу: http://127.0.0.1:5000

## 🛠 Используемые технологии

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF4500?style=for-the-badge)![WTForms](https://img.shields.io/badge/Wtforms-0052CC?style=for-the-badge)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge)![Flask-Migrate](https://img.shields.io/badge/Flask--Migrate-lightgrey?style=for-the-badge)

## 👤 Автор
[Вильмен Абрамян](https://github.com/VilmenAbramian), vilmen.abramian@gmail.com

Спринт 21
