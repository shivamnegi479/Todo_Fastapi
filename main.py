from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import uvicorn
from pymongo import MongoClient
app=FastAPI()

class Notes(BaseModel):
    title: str
    content: str


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn=MongoClient('mongodb+srv://shivamnegi479:265472@cluster0.fnxn5lx.mongodb.net/')
# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     docs=conn.fastapi.fastapi.find({})
#     newdoc=[]
#     print(docs)
#     for i in docs:
#         # print(i)
#         newdoc.append({"id":i["_id"],"Notes":i["title"],"Content":i["content"]})

#     return templates.TemplateResponse("index.html", {"request": request,"notes":newdoc})


# @app.post("/create_notes/")
# async def create_user(notes: Notes):
#     note_data = notes.dict()
#     notes_id = conn.fastapi.fastapi.insert_one(note_data).inserted_id
    
#     return {"user_id": str(notes_id),"Message":"Notes Created Successfully","Title":note_data["title"]}

if __name__=="__main__":
    uvicorn.run(app="main:app",host="localhost",reload=True)