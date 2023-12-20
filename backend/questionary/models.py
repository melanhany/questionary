import datetime
from typing import List, Optional, Union
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


class GenreRead(GenreBase):
    id: int
    games: List["Game"] = []


# class ImageBase(SQLModel):
#     url: str
#     name: str


# class Image(ImageBase, table=True):
#     __tablename__ = "images"

#     id: int = Field(default=None, nullable=False, primary_key=True)


class GameBase(SQLModel):
    game_name: str
    img_url: Optional[str]

    # image: Union[Image, None] = None


class Game(GameBase, table=True):
    __tablename__ = "games"
    id: int = Field(default=None, nullable=False, primary_key=True)
    genre_id: Optional[int] = Field(
        default=None,
        nullable=True,
        foreign_key="genres.id",
    )
    genre: Genre = Relationship(
        back_populates="games",
    )


class GameRead(GameBase):
    id: int
    genre_id: Optional[int]
    genre: Optional[Genre]


class GameCreate(GameBase):
    pass


# After the definition of `CallRead`, update the forward reference to it:
GenreRead.update_forward_refs()
