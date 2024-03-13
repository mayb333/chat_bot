import uvicorn
from fastapi import FastAPI

from src.routers.main import router as router_main

app = FastAPI()

app.include_router(router_main)
