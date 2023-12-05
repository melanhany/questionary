from typing import Union
from fastapi import FastAPI
from questionary.api import users

app = FastAPI()

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
