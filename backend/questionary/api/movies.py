from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from questionary.models import Movie, MovieCreate, MovieRead
from questionary.database import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/movies", response_model=List[MovieRead])
async def get_movies(
    skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)
):
    result = await session.exec(select(Movie).offset(skip).limit(limit))
    movies = result.all()
    return [Movie(**movie.dict()) for movie in movies]


@router.get("/movies/{movie_id}", response_model=MovieRead)
async def get_movie(movie_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Movie).where(Movie.id == movie_id))
    movie = result.first()

    if not movie:
        raise HTTPException(status_code=400, detail="Movie not found")
    return Movie(**movie.dict())


@router.post("/movies")
async def add_movie(movie: MovieCreate, session: AsyncSession = Depends(get_session)):
    movie = Movie(**movie.dict())
    session.add(movie)
    await session.commit()
    await session.refresh(movie)
    return movie


@router.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Movie).where(Movie.id == movie_id))
    movie = result.first()

    if not movie:
        raise HTTPException(status_code=400, detail="Movie not found")
    await session.delete(movie)
    await session.commit()

    return
