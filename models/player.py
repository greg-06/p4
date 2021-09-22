from pydantic import BaseModel, validator
from pydantic.types import PositiveInt
from enum import Enum
import re
from datetime import date
from utilities.fonctions import from_birthdate_to_age


class Gender(str, Enum):
    """création d'un type de variable
    qui ne peut avoir que 2 valeurs (M ou F) """
    male = "M"
    female = "F"


class Player(BaseModel):
    """création de la classe 'Player' qui a pour attributs
    l'id, le prénom, le nom, la date de naissance, le sexe
    et le classement d'un joueur
    validateur pour le prénom et le nom avec les caractères autorisés
    validateur pour la date de naissance en vérifiant l'âge légal du joueur
    (18 ans minimum)"""
    id: PositiveInt
    first_name: str
    last_name: str
    birthdate: date
    gender: Gender
    rank: PositiveInt

    @validator("first_name", "last_name")
    def check_name(cls, v: str):
        """validateur qui s'assure que les paramètres du prénom et du nom
        contiennent uniquement les caractères passés dans notre regex
            si les caractères ne correspondent pas
                renvoie une erreur
            on renvoie la valeur avec une majuscule en début de phrase"""
        if not re.match(r"^[A-Za-z \-'çéèàâêîôûäëïöü]{2,18}$", v):
            raise ValueError("Votre nom n'est pas valide")
        return v.title()

    @validator("birthdate")
    def check_age(cls, v: date):
        """validateur qui s'assure que la date de naissance
        correspond aux critères de validation
            si la date de naissance est inférieur à 18 ans
                renvoie une erreur
        on renvoie la valeur"""
        if from_birthdate_to_age(v) < 18:
            raise ValueError("Vous n'avez pas l'âge légal pour vous inscrire")
        return v


# player = Player(
#     id=1,
#     first_name="Luc",
#     last_name="skywalker",
#     birthdate="1988-02-28",
#     gender="M",
#     rank=1
# )

# print(player)
