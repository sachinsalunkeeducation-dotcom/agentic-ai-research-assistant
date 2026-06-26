from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

from orchestrator import Orchestrator

from services.stream_service import StreamService

app = FastAPI(
    title="Agentic AI System",
    description="Multi-Agent AI Task Execution System",
    version="1.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")




class UserRequest(BaseModel):
    query: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request
        }
    )

@app.get("/status")
async def get_status():

    return {
        "messages": StreamService.get_messages()
    }


@app.post("/generate-report")
async def generate_report(request: UserRequest):

    StreamService.clear()

    orchestrator = Orchestrator()

    report = await orchestrator.run(request.query)

    return {
        "query": request.query,
        "report": report
    }

# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):

#     return templates.TemplateResponse(
#         "index.html",
#         {
#             "request": request,
#             "title": "Sachin"
#         }
#     )