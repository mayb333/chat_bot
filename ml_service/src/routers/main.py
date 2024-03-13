from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def basic_func():
    return "hello"