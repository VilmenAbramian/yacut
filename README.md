# YaCut :scissors:
Автор: [Абрамян Вильмен Левонович](vilmen.abramian@gmail.com)  

## Используемые технологии
:snake: Python, Flask, Sqlalchemy, Wtforms, Flask-migrate, Jinja2

## Структура проекта
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

## Описание проекта
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или автоматически генерирует сервис.

Ключевые возможности сервиса:
 - генерация коротких ссылок и связь их с исходными длинными ссылками;
 - переадресация на исходный адрес при обращении к коротким ссылкам.

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
 - поле для длинной исходной ссылки (обязательное для заполнения);
 - поле для пользовательского варианта короткой ссылки (необязательное для заполнения).

Пользовательский вариант короткой ссылки не должен превышать 16 символов.


## Заполнение конфигурационного .env файла

```
FLASK_APP=yacut
FLASK_DEBUG=1
DATABASE_URI=ChooseDataBase
SECRET_KEY=Your!$ecretKey8

Example:
DATABASE_URI=sqlite:///db.sqlite3
```

## Запуск проекта
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

Спринт 21