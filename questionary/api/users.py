from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from questionary.models import User, UserCreate
from questionary.database import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/users", response_model=list[User])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User))
    users = result.all()
    return [User(**user.dict()) for user in users]


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User).where(User.id == user_id))
    user = result.first()

    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return User(**user.dict())


@router.post("/users")
async def add_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    user = User(**user.dict())
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User).where(User.id == user_id))
    user = result.first()
    print(user)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    await session.delete(user)
    await session.commit()

    return
