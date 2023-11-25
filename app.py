from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()

templates = Jinja2Templates(directory="templates")
