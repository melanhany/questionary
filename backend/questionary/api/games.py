from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from questionary.models import Game, GameCreate, GameRead
from questionary.database import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/games", response_model=List[GameRead])
async def get_games(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Game))
    games = result.all()
    return [Game(**game.dict()) for game in games]


@router.get("/games/{game_id}", response_model=GameRead)
async def get_game(game_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Game).where(Game.id == game_id))
    game = result.first()

    if not game:
        raise HTTPException(status_code=400, detail="Game not found")
    return Game(**game.dict())


@router.post("/games")
async def add_game(game: GameCreate, session: AsyncSession = Depends(get_session)):
    game = Game(**game.dict())
    session.add(game)
    await session.commit()
    await session.refresh(game)
    return game


@router.delete("/games/{game_id}")
async def delete_game(game_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(Game).where(Game.id == game_id))
    game = result.first()

    if not game:
        raise HTTPException(status_code=400, detail="Game not found")
    await session.delete(game)
    await session.commit()

    return
