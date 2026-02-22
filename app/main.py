from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.api.routes import router

app = FastAPI(title="WiFi CCTV Stream")

app.include_router(router)

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})