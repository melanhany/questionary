from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlalchemy.orm import joinedload
from questionary.models import Genre, GenreRead
from questionary.database import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/genres", response_model=List[GenreRead])
async def get_genres(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Genre))
    genres = result.unique().all()
    return [Genre(**genre.dict()) for genre in genres]


@router.get("/genres/{genre_id}", response_model=GenreRead)
async def get_genre(genre_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Genre).where(Genre.id == genre_id))
    genre = result.first()

    if not genre:
        raise HTTPException(status_code=400, detail="Genre not found")
    return Genre(**genre.dict())
