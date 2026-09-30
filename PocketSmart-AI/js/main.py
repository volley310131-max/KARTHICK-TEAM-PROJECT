from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

try:
    from .gemini_utils import (
        get_home_recommendations,
        get_party_recommendations,
        get_jewelry_recommendations,
    )
except ImportError:  # pragma: no cover - fallback for direct script execution
    from gemini_utils import (
        get_home_recommendations,
        get_party_recommendations,
        get_jewelry_recommendations,
    )

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@app.post("/login", response_class=HTMLResponse)
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    return HTMLResponse(
        f"<h1>Welcome {username}!</h1>"
        "<p>Login successful.</p>"
        "<a href='/'>Go Home</a>"
    )


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )


@app.post("/register", response_class=HTMLResponse)
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    return HTMLResponse(
        f"<h1>Registration Successful!</h1>"
        f"<p>Welcome {username}.</p>"
        "<a href='/login'>Go to Login</a>"
    )
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/home", response_class=HTMLResponse)
async def home_planner_page(request: Request):
    return templates.TemplateResponse(request=request, name="home_planner.html")


@app.get("/party", response_class=HTMLResponse)
async def party_planner_page(request: Request):
    return templates.TemplateResponse(request=request, name="party_planner.html")


@app.get("/jewelry", response_class=HTMLResponse)
async def jewelry_planner_page(request: Request):
    return templates.TemplateResponse(request=request, name="jewelry_planner.html")


@app.post("/generate-home", response_class=HTMLResponse)
async def generate_home(
    request: Request,
    budget: float = Form(...),
    room: str = Form(...),
    style: str = Form(...)
):
    result = get_home_recommendations(
        budget,
        room,
        style
    )

    return templates.TemplateResponse(
        request=request,
        name="home_planner.html",
        context={
            "result": result
        }
    )


@app.post("/generate-party", response_class=HTMLResponse)
async def generate_party(
    request: Request,
    budget: float = Form(...),
    guests: int = Form(...),
    event_type: str = Form(...),
    venue: str = Form(...)
):
    result = get_party_recommendations(
        budget,
        guests,
        event_type,
        venue
    )

    return templates.TemplateResponse(
        request=request,
        name="party_planner.html",
        context={
            "result": result
        }
    )


@app.post("/generate-jewelry", response_class=HTMLResponse)
async def generate_jewelry(
    request: Request,
    budget: float = Form(...),
    occasion: str = Form(...),
    style: str = Form(...)
):
    result = get_jewelry_recommendations(
        budget,
        occasion,
        style
    )

    return templates.TemplateResponse(
        request=request,
        name="jewelry_planner.html",
        context={
            "result": result
        }
    )


@app.get("/health")
async def health():
    return {
        "status": "PocketSmart AI is running"
    }