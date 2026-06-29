# Board — Admin Dashboard

> A Django-powered admin dashboard web application. Built with Python, Django, HTML/CSS, and SQLite.

---

## Tech Stack

| Layer     | Technology                        |
| --------- | --------------------------------- |
| Framework | Django (Python)                   |
| Database  | SQLite (`db.sqlite3`)             |
| Templates | Django HTML Templates             |
| Styling   | CSS (custom styles)               |
| Auth      | Django built-in auth system       |

---

## Project Structure

```
board/
├── dashboard/            # Django project config (settings, urls, wsgi)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/                # Main Django app
│   ├── migrations/       # Database migrations
│   ├── templates/        # HTML templates
│   ├── models.py         # Data models
│   ├── views.py          # View logic
│   ├── urls.py           # App URL routes
│   └── admin.py          # Django admin config
├── db.sqlite3            # SQLite database
└── manage.py             # Django management CLI
```

---

## Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/sulaimonazeez/board.git
cd board
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install django
```

> If a `requirements.txt` exists, run `pip install -r requirements.txt` instead.

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
# → http://127.0.0.1:8000
```

---

## Access

| URL              | Description              |
| ---------------- | ------------------------ |
| `/`              | Dashboard home           |
| `/admin/`        | Django admin panel       |

Log in with the superuser credentials you created above.

---

## Database

The project uses **SQLite** by default (`db.sqlite3`), which requires zero configuration. To switch to PostgreSQL or MySQL for production, update `DATABASES` in `dashboard/settings.py`.

---

## Useful Commands

```bash
# Run server
python manage.py runserver

# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Open Django shell
python manage.py shell

# Collect static files (for production)
python manage.py collectstatic
```

---

## Deployment Notes

For production deployment:

1. Set `DEBUG = False` in `dashboard/settings.py`
2. Set a strong `SECRET_KEY` via environment variable
3. Add your domain to `ALLOWED_HOSTS`
4. Switch to PostgreSQL or MySQL
5. Run `python manage.py collectstatic`
6. Serve with **Gunicorn** behind **Nginx**

---

## License

Private — © sulaimonazeez. All rights reserved.
