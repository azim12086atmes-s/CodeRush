from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import datetime

app = FastAPI(title="Code Rush - Second Brain API")

# --- DATA MODELS (The Shape of our Thoughts) ---
class NoteInput(BaseModel):
    content: str
    media_type: str = "text" # text, audio, image
    tags: List[str] = []

class Note(NoteInput):
    id: int
    created_at: str

# --- IN-MEMORY STORE (Temporary, until we add Supabase) ---
fake_db = []

@app.get("/")
def read_root():
    return {"status": "System Operational", "notes_count": len(fake_db)}

@app.post("/notes/", response_model=Note)
def create_note(note: NoteInput):
    # This is where the AI logic will eventually go!
    new_note = Note(
        id=len(fake_db) + 1,
        created_at=datetime.datetime.now().isoformat(),
        **note.dict()
    )
    fake_db.append(new_note)
    return new_note

@app.get("/notes/")
def get_notes():
    return fake_db
