from typing import List
from pydantic import BaseModel, validator
from pydantic.types import PositiveInt
import re
from datetime import datetime
from .turn import Turn


class Tournament(BaseModel):
    id: PositiveInt
    name: str
    place: str
    date_start: datetime
    date_end: datetime
    nb_turns: PositiveInt
    players: List[PositiveInt]
    turns: List[Turn]

    @validator("name", "place")
    def check_name(cls, v: str):
        if not re.match(r"^[A-Za-z \-'çéèàâêîôûäëïöü]{2,25}$", v):
            raise ValueError("Votre nom n'est pas valide")
        return v.title()
