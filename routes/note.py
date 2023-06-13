from fastapi import APIRouter,HTTPException
from models.note import Note
from schema.note import noteEntity,notesEntity
from config.db import conn
from fastapi import Request
from bson import ObjectId
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
note =APIRouter()
from typing import Dict

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.fastapi.fastapi.find({})
    newdoc=[]
    print(docs)
    for i in docs:
        newdoc.append({"id":i["_id"],"title":i["title"],"desc":i["desc"],"important":i["important"]})
    return templates.TemplateResponse("index.html", {"request": request,"notes":newdoc})


@note.get("/{id}")
async def read_item2(request: Request,id:str):
    docs=conn.fastapi.fastapi.find_one({"_id": ObjectId(id)})

        # newd
        # newdoc.append({"id":i["_id"],"title":i["title"],"desc":i["desc"],"important":i["important"]})
        # print(i,j)
    return templates.TemplateResponse("note.html", {"request": request,"notes":docs})
# @note.get("/t", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs=conn.fastapi.fastapi.find({})
#     newdoc=[]
#     print(docs)
#     for i in docs:
#         newdoc.append({"id":i["_id"],"title":i["title"],"desc":i["desc"],"important":i["important"]})
#     return templates.TemplateResponse("index.html", {"request": request,"notes":newdoc})
@note.post("/")
async def create_user(request:Request):
    form=await request.form()
    docs=conn.fastapi.fastapi.find({})
    newdoc=[]
    data=dict(form)
    print(data)
    for i in docs:
        newdoc.append({"id":i["_id"],"title":i["title"],"desc":i["desc"],"important":i["important"]})
    if "important" not in data.keys():
        data["important"]=False
    else:
        data["important"]=True 
   
    if conn.fastapi.fastapi.find_one({"title": data['title']}):
        raise HTTPException(status_code=400, detail="Note with the same title already exists.")
    notes_id = conn.fastapi.fastapi.insert_one(data)
    return templates.TemplateResponse("index.html", {"request": request,"notes":newdoc,"status":f"{data['title']} createad Successfully"})


