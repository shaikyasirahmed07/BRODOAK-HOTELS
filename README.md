# BRODOAK-HOTELS

# Django Full-Stack Web Application

This is a full-stack web application built using the Django framework. The application utilizes HTML and CSS for the frontend and Django for the backend. Follow the instructions below to set up and run the project on your local machine.

## Prerequisites

Before starting, ensure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Django 4.0+](https://www.djangoproject.com/download/)
- [pip (Python package installer)](https://pip.pypa.io/en/stable/installation/)
- [Git (optional)](https://git-scm.com/downloads)

## Project Setup

### 1. Clone the Repository (Optional)

If the project is hosted on a version control platform like GitHub, clone the repository using:

```bash
git clone https://github.com/yourusername/your-django-project.git
```
## 2. Create a Virtual Environment
- Navigate to the project directory and create a virtual environment to isolate dependencies:
```bash
cd your-django-project
python -m venv env

```


## 3. Activate the Virtual Environment
- Windows:
```bash
.\env\Scripts\activate
```


- Linux/Mac:
```bash
source env/bin/activate
```


## 4. Install Dependencies
- Install the required Python packages from requirements.txt:
```bash
pip install -r requirements.txt
```
## If you don't have a requirements.txt file, manually install Django:
```bash
pip install django
```
## 5. Create Django Project (If Not Already Created)
- If you don't have a Django project set up yet, create one using:

```bash
django-admin startproject project_name
```

- Navigate to the project directory:
```bash
cd project_name
```


## 6. Create Django App (If Not Already Created)
- If you don't have a Django app set up, create one using:
```bash
python manage.py startapp app_name
```


## 7. Configure settings.py
- In the project_name/settings.py file, add your app to the INSTALLED_APPS list:
```bash
INSTALLED_APPS = [
    ...
    'app_name',
]
```

- Set up static files and templates:
```bash
STATIC_URL = '/static/'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    },
]

```

## 8. Set Up HTML and CSS
- Create a templates folder in your app directory (e.g., app_name/templates/app_name/) and add your HTML files there.
- Create a static folder in your app directory (e.g., app_name/static/app_name/) and add your CSS files there.


 ## 9. Create Database Migrations
- Create database migrations based on your models:
```bash
python manage.py makemigrations
python manage.py migrate
```



## 10. Create a Superuser (Admin)
- Create an admin user to access the Django admin panel:
```bash
python manage.py createsuperuser
```


## 11. Run the Development Server
- Run the Django development server:
```bash
python manage.py runserver

```



- Open your browser and navigate to http://127.0.0.1:8000/ to view the application.
## Project Structure
```bash
hotel/
│
├── home/
│   ├──hotel/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── hotels/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── app_name/
│   │   │       └── index.html
│   │   ├── static/
│   │   │   └── app_name/
│   │   │       ├── style.css
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   ├── manage.py
│   └── db.sqlite3
├── requirements.txt
└── README.md

```
## How to Contribute
- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Commit your changes (git commit -am 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Create a new Pull Request.
