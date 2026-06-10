# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework. Students will create a small CRUD service, practice request/response handling, validation with Pydantic, and run the app with Uvicorn.

## 📝 Tasks

### 🛠️ Implement a CRUD API for Items

#### Description
Create a FastAPI application that exposes endpoints to create, read, update, and delete `Item` resources. Use Pydantic models for request and response validation and maintain a simple in-memory store (dictionary) for data persistence during runtime.

#### Requirements
Completed program should:

- Define a Pydantic `Item` model with `id: int`, `name: str`, and optional `description: str`.
- Implement the following endpoints:
  - `GET /items` — return a list of items.
  - `GET /items/{item_id}` — return a single item by id (404 if not found).
  - `POST /items` — create a new item and return it (assign an `id`).
  - `PUT /items/{item_id}` — update an existing item (404 if not found).
  - `DELETE /items/{item_id}` — delete an item (404 if not found).
- Validate request payloads using Pydantic models.
- Return appropriate HTTP status codes and JSON responses.
- Include inline documentation/comments explaining key parts of the code.

#### Example Requests

Create an item:

```bash
curl -s -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d '{"name":"Widget","description":"A test widget"}'
```

Get all items:

```bash
curl -s "http://127.0.0.1:8000/items"
```

Update an item:

```bash
curl -s -X PUT "http://127.0.0.1:8000/items/1" -H "Content-Type: application/json" -d '{"name":"Updated","description":"Updated desc"}'
```

Run the app (development):

```bash
pip install -r requirements.txt
uvicorn starter_code:app --reload
```

Optional enhancements (not required):

- Persist data to a local JSON file or SQLite DB.
- Add pagination or search query parameters to `GET /items`.
- Add automated tests using `requests` or `httpx` and `pytest`.

***

