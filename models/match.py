from pydantic.main import BaseModel
from pydantic.types import PositiveInt


class Match(BaseModel):
    id_p1: PositiveInt
    id_p2: PositiveInt
    s1: float
    s2: float
