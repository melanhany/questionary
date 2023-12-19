import datetime
from lib2to3.pgen2.grammar import opmap_raw
from typing import List, Optional
from sqlalchemy import null
from sqlmodel import SQLModel, Field, Relationship


class UserBase(SQLModel):
    first_name: str
    last_name: str
    birth_date: datetime.date
    programming_language: str


class User(UserBase, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, nullable=False, primary_key=True)


class UserCreate(UserBase):
    pass


class GenreBase(SQLModel):
    genre_name: str


class Genre(GenreBase, table=True):
    __tablename__ = "genres"
    id: int = Field(default=None, nullable=False, primary_key=True)

    games: List["Game"] = Relationship(back_populates="genre")


class GameBase(SQLModel):
    game_name: str
    img_url: Optional[str]


class Game(GameBase, table=True):
    __tablename__ = "games"
    id: int = Field(default=None, nullable=False, primary_key=True)
    genre_id: int = Field(default=None, nullable=False, foreign_key="genres.id")

    genre: Genre = Relationship(back_populates="games")

class GameCreate(GameBase):
    pass