from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config.db import conn

note = APIRouter()
templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    
   # doc = conn.notes.notes.find_one({})

    cursor = conn.notes.notes.find({})
    newDocs = []
    for doc in cursor:
        if doc:
            newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],  
            "desc": doc["desc"],
            "important": doc["important"]
        })
   
    return templates.TemplateResponse("index.html", {"request": request, "newDocs": newDocs})

@note.post("/")
async def create_note(request: Request):
    form = await request.form()
    print(form)
    formDict = dict(form)
    formDict["important"] = True
    if formDict["important"] == "on":
        important = True
    else:
        important = False

    note = conn.notes.notes.insert_one(formDict)
    return {"Success": False} if important else {"Success": True}

