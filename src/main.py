from fastapi import FastAPI

from settings import envariables

app = FastAPI()


@app.get("/")
async def root():
    return envariables.model_dump_json()
