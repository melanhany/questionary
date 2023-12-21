from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from questionary.api import movies, genres

from questionary.models import (
    MovieGenreLink,
    Genre,
    GenreRead,
    Movie,
    MovieCreate,
    MovieRead,
)

app = FastAPI()

app.mount("/imgs", StaticFiles(directory="imgs"), name="images")

app.include_router(genres.router)
app.include_router(movies.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
