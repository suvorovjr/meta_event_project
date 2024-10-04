from pydantic import BaseModel
from typing import List


class PagesDataModel(BaseModel):
    access_token: str
    category: str
    name: str
    id: str


class PagesResponseModel(BaseModel):
    data: List[PagesDataModel]
