from fastapi import APIRouter,HTTPException
from models.note import Note
from schema.note import noteEntity,notesEntity
from config.db import conn
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
note =APIRouter()
from pydantic import BaseModel
templates = Jinja2Templates(directory="templates")

# class User(BaseModel):
#     name:str
#     email:str
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.fastapi.fastapi.find({})
    newdoc=[]
    print(docs)
    for i in docs:
        newdoc.append({"id":i["_id"],"title":i["title"],"desc":i["desc"],"important":i["important"]})
    return templates.TemplateResponse("index.html", {"request": request,"notes":newdoc})

@note.post("/create_notes/")
async def create_user(notes: Note):
    note_data = notes.dict()
    print(notes)
    print(note_data["title"])
    if conn.fastapi.fastapi.find_one({"title": note_data['title']}):
        raise HTTPException(status_code=400, detail="Note with the same title already exists.")
    notes_id = conn.fastapi.fastapi.insert_one(note_data).inserted_id
    return {"Message":"Notes Created Successfully","note":notes}