from typing import Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    id: int
    text: str

# In-memory store
notes: Dict[int, Note] = {}
_next_id = 1

@app.get("/notes")
def list_notes():
    return list(notes.values())

class NoteCreate(BaseModel):
    text: str

@app.post("/notes", status_code=201)
def create_note(payload: NoteCreate):
    """Create a note and assign a server-side id."""
    global _next_id
    note = Note(id=_next_id, text=payload.text)
    notes[_next_id] = note
    _next_id += 1
    return note

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("starter_code:app", host="127.0.0.1", port=8000, reload=True)
