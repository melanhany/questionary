from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def read_root():
    return {"Hello": "World"}
