
# Django Posts API

A simple Django + Django REST Framework backend that provides:

- User login (session-based)
- User logout
- Password change
- Get current user (`/me`)
- CRUD for posts (each user sees/manages only their own posts)

Works perfectly with any React frontend.

## Features

- Session-based authentication
- Django password validation
- CRUD operations for posts
- Ownership enforcement
- Clean project structure

## API Endpoints

### Auth
- `POST /api/auth/login/`
- `POST /api/auth/logout/`
- `GET /api/auth/me/`
- `POST /api/auth/password-change/`

### Posts
- `GET /api/posts/`
- `POST /api/posts/`
- `GET /api/posts/<id>/`
- `PUT /api/posts/<id>/`
- `PATCH /api/posts/<id>/`
- `DELETE /api/posts/<id>/`

## Installation

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
# .\venv\Scripts\activate  # Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## React Usage

```js
axios.post("/api/auth/login/", data, { withCredentials: true })
```

## Project Structure

```
config/
posts/
manage.py
requirements.txt
```
