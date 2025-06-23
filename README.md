# Late Show API

A Flask RESTful API for managing guests, episodes, and appearances for a talk show.

## Features
- User registration and login with JWT authentication
- CRUD for guests, episodes, and appearances
- PostgreSQL database with SQLAlchemy and Flask-Migrate

## Setup

### 1. Install dependencies
```
pipenv install --dev
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
pipenv shell
```

### 2. PostgreSQL DB setup
Create your database in Postgres:
```
psql -U postgres
CREATE DATABASE late_show_db;
```

### 3. Set your DATABASE_URI in `server/config.py`
```
SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
```

### 4. Run DB setup
```
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
python server/seed.py
```

### 5. Run the server
```
flask run
```

## API Endpoints
See `challenge-4-lateshow.postman_collection.json` for example requests.

- `POST /register` — Register a new user
- `POST /login` — Login and get JWT
- `GET /guests` — List all guests
- `GET /episodes` — List all episodes
- `POST /appearances` — Create an appearance (JWT required)

## Notes
- Default admin user: `admin` / `password`
- Update your DB credentials in `server/config.py` as needed.
- For development only. Do not use in production as-is.
