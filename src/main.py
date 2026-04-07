from fastapi import FastAPI
from src.api.routers.link_routers import router


app = FastAPI()


app.include_router(router)