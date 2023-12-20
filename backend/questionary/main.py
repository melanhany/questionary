from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from questionary.api import users, genres, games

from questionary.models import (
    User,
    UserCreate,
    Genre,
    GenreRead,
    Game,
    GameCreate,
    GameRead,
)

app = FastAPI()

app.mount("/imgs", StaticFiles(directory="imgs"), name="images")

app.include_router(users.router)
app.include_router(genres.router)
app.include_router(games.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
