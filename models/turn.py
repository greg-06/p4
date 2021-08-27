from datetime import datetime
from typing import List
from pydantic.main import BaseModel
from pydantic.types import PositiveInt


class Turn(BaseModel):
    name: str
    date_start: datetime
    date_end: datetime
    matchs: List[PositiveInt]
