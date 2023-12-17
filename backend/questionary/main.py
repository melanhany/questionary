from typing import Union
from fastapi import FastAPI
from questionary.api import users

from questionary.models import User, UserCreate


app = FastAPI()

app.include_router(users.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
