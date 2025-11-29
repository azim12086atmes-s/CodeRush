from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
# Import our new database functions
from db import add_note_to_db, get_all_notes

app = FastAPI(title="Code Rush - Second Brain API")

# --- DATA MODELS ---
class NoteInput(BaseModel):
    content: str
    media_type: str = "text" # text, audio, image
    tags: List[str] = []

class Note(BaseModel):
    id: int
    content: str
    category: str
    tags: Optional[List[str]] = None
    created_at: str

@app.get("/")
def read_root():
    return {"status": "System Operational", "mode": "Database Connected"}

@app.post("/notes/")
def create_note(note: NoteInput):
    # Save to Supabase
    try:
        new_note = add_note_to_db(note.content, note.tags, note.media_type)
        return new_note
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/notes/")
def get_notes():
    # Fetch from Supabase
    return get_all_notes()
