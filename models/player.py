from pydantic import BaseModel, validator
from pydantic.types import PositiveInt
from enum import Enum
import re
from datetime import date
from utilities.fonctions import from_birthdate_to_age


class Gender(str, Enum):
    male = "M"
    female = "F"


class Player(BaseModel):
    id: PositiveInt
    first_name: str
    last_name: str
    birthdate: date
    gender: Gender
    rank: PositiveInt

    @validator("first_name", "last_name")
    def check_name(cls, v: str):
        if not re.match(r"^[A-Za-z \-'çéèàâêîôûäëïöü]{2,18}$", v):
            raise ValueError("Votre nom n'est pas valide")
        return v.title()

    @validator("birthdate")
    def check_age(cls, v: date):
        if from_birthdate_to_age(v) < 18:
            raise ValueError("Vous n'avez pas l'âge légal pour vous inscrire")
        return v


player = Player(
    id=1,
    first_name="Luc",
    last_name="skywalker",
    birthdate="1988-02-28",
    gender="M",
    rank=1
)

print(player)
