# Tati TODO API

A RESTful API for managing TODO items, built with Django and Django REST Framework.

**Live Demo:** [https://tati-todo-api.onrender.com/api/todos/](https://tati-todo-api.onrender.com/api/todos/)

## Tech Stack

- Python 3.12
- Django 6.0
- Django REST Framework 3.17
- Gunicorn (production WSGI server)
- WhiteNoise (static file serving)
- Docker & Docker Compose
- SQLite
- Deployed on Render

## API Endpoints

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| GET | `/api/todos/` | List all todos | 200 |
| POST | `/api/todos/` | Create a new todo | 201 |
| GET | `/api/todos/<id>/` | Retrieve a single todo | 200 |
| PUT | `/api/todos/<id>/` | Update a todo (full) | 200 |
| DELETE | `/api/todos/<id>/` | Delete a todo | 204 |

## Request & Response Examples

### Create a Todo

**Request:**

```json
POST /api/todos/
Content-Type: application/json

{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread, and coffee"
}
```

**Response (201 Created):**

```json
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread, and coffee",
    "is_completed": false,
    "created_at": "2026-05-20T08:00:00.000000Z",
    "updated_at": "2026-05-20T08:00:00.000000Z"
}
```

### Update a Todo

**Request:**

```json
PUT /api/todos/1/
Content-Type: application/json

{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread, coffee, and butter",
    "is_completed": true
}
```

**Response (200 OK):**

```json
{
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread, coffee, and butter",
    "is_completed": true,
    "created_at": "2026-05-20T08:00:00.000000Z",
    "updated_at": "2026-05-20T09:30:00.000000Z"
}
```

### Validation Errors

Titles and descriptions must be at least 3 characters. Missing or invalid fields return a `400 Bad Request`:

```json
{
    "title": ["Ensure this field has at least 3 characters."]
}
```

## Getting Started

### Prerequisites

- Python 3.12+
- Docker & Docker Compose (for containerized setup)

### Run with Docker (recommended)

```bash
git clone https://github.com/Ckola99/tati-todo-api.git
cd tati-todo-api
docker-compose up --build
```

The API will be available at `http://localhost:8000/api/todos/`.

### Run without Docker

```bash
git clone https://github.com/Ckola99/tati-todo-api.git
cd tati-todo-api
python -m venv venv
source venv/Scripts/activate    # Windows/Git Bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/todos/`.

## Running Tests

```bash
python manage.py test todos
```

The test suite covers:

- Creating a todo (valid data → 201)
- Listing all todos (GET → 200)
- Retrieving a single todo (GET by ID → 200)
- Updating a todo (PUT → 200)
- Deleting a todo (DELETE → 204)
- Validation: title too short (→ 400)
- Validation: missing required fields (→ 400)
- Retrieving a non-existent todo (→ 404)

## Postman Collection

A Postman collection is included in the repository: `tati-todo-api.postman_collection.json`

**To use it:**

1. Import the collection file into Postman
2. The `base_url` variable is pre-configured to the live deployment
3. Run **Create Todo** first — the returned ID is automatically stored and used by Retrieve, Update, and Delete requests
4. To test locally, update the `base_url` variable to `http://localhost:8000/api`

## Environment Variables

Sensitive configuration is managed through environment variables. See `.env.example` for the required variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `your-secret-key-here` |
| `DEBUG` | Enable debug mode | `False` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost` |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated trusted origins | `http://localhost:8000` |

## Project Structure

```
tati-todo-api/
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todos/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── tati-todo-api.postman_collection.json
├── manage.py
└── README.md
```

## Logging

The API logs key operations to the console:

- `INFO` — todo created, updated, or deleted (with ID)
- `ERROR` — failed operations (with error details)

Logging is configured for the `todos` app at `INFO` level in `settings.py`.
