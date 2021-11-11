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
        if not re.match(r"^[A-Za-z \-'çéèàâêîôûäëïöü_0123456789()]{2,80}$", v):
            raise ValueError("Votre nom n'est pas valide")
        return v.title()

    def render_tournaments(self, lenght: int, char: str):
        return f"{str(self.id).zfill(3).ljust(lenght, char)} {self.name.ljust(lenght,char)} {self.place.ljust(lenght, char)}"

    # def __str__(self) -> str:
    #     return (f"{str(self.id).zfill(3)} {self.name} {self.place}")
