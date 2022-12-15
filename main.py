import typing
from fastapi import FastAPI
from pydantic import BaseModel
from routes.download import router as download_router
from routes.search import router as search_router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

class Config(BaseModel):
    host: str
    port: int
    cors_allowed_hosts: typing.List[str]

app = FastAPI()

with open("config.json", "r") as f:
    config = Config.parse_raw(f.read())

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.cors_allowed_hosts,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(download_router, prefix="/download", tags=["download"])
app.include_router(search_router, prefix="/search", tags=["search"])

uvicorn.run(app, host=config.host, port=config.port)