from fastapi import FastAPI

from settings import ENVARIABLES

app = FastAPI()


@app.get("/")
async def root():
    return ENVARIABLES.model_dump_json()
