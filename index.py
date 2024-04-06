from fastapi import FastAPI
from routes.note import note
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app =FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(note)