from datetime import datetime
from typing import List
from pydantic.main import BaseModel
from pydantic.types import PositiveInt
from .match import Match


class Turn(BaseModel):
    name: str
    date_start: datetime
    date_end: datetime
    matchs: List[Match]
