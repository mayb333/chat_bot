from fastapi import APIRouter

from typing import List

from src.config import PROMPT_TEMPLATE
from src.routers.schemas import Context, Prediction

router = APIRouter()


@router.get("/get_context", response_model=List[Context])
async def get_context(query: str) -> List[Context]:
    return [Context(text="Some_Context_1", url="https://some_url_1.com"),
            Context(text="Some_Context_2", url="https://some_url_2.com")]


@router.get("/predict", response_model=Prediction)
async def predict(query: str) -> Prediction:
    context = await get_context(query=query)
    print(context)
    return Prediction(text="Best answer", urls=["google.com", "yandex.ru"])
