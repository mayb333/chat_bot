from pydantic import BaseModel
from typing import List


class Context(BaseModel):
    text: str
    url: str


class Prediction(BaseModel):
    text: str
    urls: List[str]
