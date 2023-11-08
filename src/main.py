from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.orm import clear_mappers

from infrastructure.persistence.database import SQLALCHEMY_MAPPER_REGISTRY
from infrastructure.persistence.mappers import start_mappers
from presentation.routes.user_routes import router as user_router
from settings import ENVARIABLES


@asynccontextmanager
async def lifespan(app: FastAPI):  # pylint: disable=W0621, W0613
    start_mappers()
    SQLALCHEMY_MAPPER_REGISTRY.configure()
    yield
    clear_mappers()


app = FastAPI(lifespan=lifespan)

app.include_router(user_router)


@app.get("/")
async def root():
    return ENVARIABLES.model_dump_json()
