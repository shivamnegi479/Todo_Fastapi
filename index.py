from fastapi import FastAPI
from routes.note import note
from fastapi.staticfiles import StaticFiles
import uvicorn

app=FastAPI()
app.include_router(note)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__=="__main__":
    uvicorn.run(app="index:app",host="localhost",reload=True)
