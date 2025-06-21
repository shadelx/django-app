# Django CRUD University Course Application

A simple web application for managing university courses, built with Django and Bootstrap.

## Features

- Create, read, update, and delete (CRUD) university courses
- Responsive UI with Bootstrap 5
- Modular Django app structure
- SQLite database for development

## Project Structure

```
django-app/
├── Academico/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   │   ├── css/
│   │   │   └── gestion.css
│   │   └── js/
│   │       └── gestion.js
│   └── templates/
│       ├── base.html
│       ├── editarCurso.html
│       └── gestion.html
├── Universidad/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

## Setup Instructions

1. **Clone the repository**

   ```sh
   git clone <repository-url>
   cd django-app
   ```

2. **Install dependencies**

   ```sh
   pipenv install
   ```

3. **Activate the virtual environment**

   ```sh
   pipenv shell
   ```

4. **Apply migrations**

   ```sh
   python manage.py migrate
   ```

5. **Run the development server**

   ```sh
   python manage.py runserver
   ```

6. **Access the application**

   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- Use the navigation bar to access course management features.
- Add, edit, or delete courses as needed.

## Static Files

- CSS: [`Academico/static/css/gestion.css`](Academico/static/css/gestion.css)
- JS: [`Academico/static/js/gestion.js`](Academico/static/js/gestion.js)

## Templates

- Base layout: [`Academico/templates/base.html`](Academico/templates/base.html)
- Course management: [`Academico/templates/gestion.html`](Academico/templates/gestion.html)
- Edit course: [`Academico/templates/editarCurso.html`](Academico/templates/editarCurso.html)

## License

This project is for educational purposes.
