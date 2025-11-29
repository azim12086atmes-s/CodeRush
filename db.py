import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    print("Warning: Supabase credentials not found!")
    # Create a dummy client so the app doesn't crash during build, 
    # but it won't work for real data until keys are set.
    supabase = None 
else:
    supabase: Client = create_client(url, key)

def add_note_to_db(content: str, tags: list, category: str):
    if not supabase: return None
    data = {"content": content, "tags": tags, "category": category}
    response = supabase.table("notes").insert(data).execute()
    return response.data[0]

def get_all_notes():
    if not supabase: return []
    response = supabase.table("notes").select("*").execute()
    return response.data
