from fastapi import APIRouter, Depends
from sqlmodel import select
from questionary.models import User, UserCreate
from questionary.database import get_session
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter()


@router.get("/users", response_model=list[User])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.exec(select(User))
    users = result.all()
    return [
        User(id=user.id, first_name=user.first_name, last_name=user.last_name)
        for user in users
    ]
