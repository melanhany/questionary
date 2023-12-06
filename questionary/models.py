import datetime
from sqlmodel import SQLModel, Field


class UserBase(SQLModel):
    first_name: str
    last_name: str
    birth_date: datetime.date
    programming_language: str


class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class UserCreate(UserBase):
    pass
