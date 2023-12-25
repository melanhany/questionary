from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from questionary.api import movies, genres, users

from questionary.models import (
    MovieGenreLink,
    Genre,
    GenreRead,
    Movie,
    MovieCreate,
    MovieRead,
    User,
    UserCreate,
    UserRead,
)

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/imgs", StaticFiles(directory="imgs"), name="images")

app.include_router(genres.router)
app.include_router(movies.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
