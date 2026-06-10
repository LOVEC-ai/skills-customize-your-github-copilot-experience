# 📘 Assignment: FastAPI Intro Lab

## 🎯 Objective

Quick, hands-on introduction to building a minimal REST API with FastAPI. Students will implement two endpoints (list and create), validate input with Pydantic, and run the app locally with Uvicorn.

## 📝 Tasks

### 🛠️ Build a Minimal Notes API

#### Description
Create a tiny FastAPI application that manages `Note` objects in-memory. Implement `GET /notes` to return all notes and `POST /notes` to create a new note. Use a Pydantic model for validation and keep the implementation small enough to complete in 30–60 minutes.

#### Requirements
Completed program should:

- Define a `Note` Pydantic model with `id: int` and `text: str`.
- Implement `GET /notes` to return a list of notes.
- Implement `POST /notes` to accept a payload with `text` and return the created note (assign a server-side `id`).
- Validate input and return appropriate HTTP status codes (e.g., 201 on create).
- Include brief inline comments explaining the main parts.

#### Example

Create a note:

```bash
curl -s -X POST "http://127.0.0.1:8000/notes" -H "Content-Type: application/json" -d '{"text":"Buy milk"}'
```

List notes:

```bash
curl -s "http://127.0.0.1:8000/notes"
```

Run locally:

```bash
pip install -r requirements.txt
uvicorn starter_code:app --reload
```

Optional extensions (stretch):

- Add `GET /notes/{id}` and `DELETE /notes/{id}`.
- Persist notes to a JSON file.
- Add simple tests using `httpx` and `pytest`.

