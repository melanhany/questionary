import datetime
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class UserBase(SQLModel):
    first_name: str
    last_name: str
    email: str


class User(UserBase, table=True):
    __tablename__ = "users"
    id: int = Field(default=None, nullable=False, primary_key=True)


class UserRead(UserBase):
    id: int


class UserCreate(UserBase):
    pass


class MovieGenreLink(SQLModel, table=True):
    genre_id: Optional[int] = Field(
        default=None, foreign_key="genres.id", primary_key=True
    )
    movie_id: Optional[int] = Field(
        default=None, foreign_key="movies.id", primary_key=True
    )


class GenreBase(SQLModel):
    genre_name: str


class Genre(GenreBase, table=True):
    __tablename__ = "genres"
    id: int = Field(default=None, nullable=False, primary_key=True)

    movies: List["Movie"] = Relationship(
        back_populates="genres", link_model=MovieGenreLink
    )


class GenreRead(GenreBase):
    id: int
    movies: List["Movie"]


# class ImageBase(SQLModel):
#     url: str
#     name: str


# class Image(ImageBase, table=True):
#     __tablename__ = "images"

#     id: int = Field(default=None, nullable=False, primary_key=True)


class MovieBase(SQLModel):
    title: str
    budget: int
    homepage: str
    overview: str
    popularity: float
    release_date: datetime.date
    revenue: int
    runtime: int
    movie_status: str
    tagline: str
    vote_average: float
    vote_count: int


class Movie(MovieBase, table=True):
    __tablename__ = "movies"
    id: int = Field(default=None, nullable=False, primary_key=True)

    genres: List["Genre"] = Relationship(
        back_populates="movies", link_model=MovieGenreLink
    )


class MovieRead(MovieBase):
    id: int

    genres: List["Genre"] = []


class MovieCreate(MovieBase):
    pass


MovieRead.update_forward_refs()
