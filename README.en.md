# ✂️ YaCut — URL Shortener

## 📖 Project Description

**YaCut** is a service for shortening long URLs.
🔑 Key features:
- Generate short links and associate them with original URLs.
- Automatic redirection from a short link to the original address.

🖥 User interface:
A single-page form with two fields:
- A field for the original long link (**required**).
- A field for a custom short link (**optional**, up to 16 characters).

## 📂 Project Structure
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

## ⚙️ `.env` Configuration
```
FLASK_APP=yacut
FLASK_DEBUG=1
DATABASE_URI=ChooseDataBase
SECRET_KEY=Your!$ecretKey8

Example:
DATABASE_URI=sqlite:///db.sqlite3
```

## 🚀 How to Run the Project
1. Clone the repository:
```bash
git clone https://github.com/VilmenAbramian/yacut.git
```
2. Create and activate a virtual environment:
```bash
python3 -m venv venv
```
For Linux/macOS:
```bash
source venv/bin/activate
```
For Windows:
```
venv\Scripts\activate.bat
```
3. Upgrade pip and install dependencies:
 ```requirements.txt```
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
4. Create the **.env** file and fill it according to the recommendations:
```bash
touch .env
```
5. Run database migrations:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
6. 6.  Start the project:
```bash
flask run
```
Once launched, the service will be available at: http://127.0.0.1:5000

## 🛠 Technologies Used

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF4500?style=for-the-badge)![WTForms](https://img.shields.io/badge/Wtforms-0052CC?style=for-the-badge)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge)![Flask-Migrate](https://img.shields.io/badge/Flask--Migrate-lightgrey?style=for-the-badge)

## 👤 Author
[Vilmen Abramian](https://github.com/VilmenAbramian), vilmen.abramian@gmail.com

Sprint 21
