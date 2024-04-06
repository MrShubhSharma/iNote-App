from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

conn = MongoClient("mongodb+srv://shubhs:y3XkIZKJxiTbwlA5@cluster0.okk2gid.mongodb.net/")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find_one({}) 
    newDocs =[]
    for doc in docs:
        newDocs.append({
            "id": docs["_id"],
            "notes": docs["notes"]
        })
    return templates.TemplateResponse("index.html", {"request":request, "newDocs": newDocs})
