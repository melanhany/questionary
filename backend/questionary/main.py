from typing import Union
from fastapi import FastAPI
from questionary.api import users, genres

from questionary.models import User, UserCreate, Genre

app = FastAPI()

app.include_router(users.router)
app.include_router(genres.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
