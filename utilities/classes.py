import re


class Name(str):
    def __new__(cls, value):
        if not re.match(r"^[A-Za-z \-'çéèàâêîôûäëïöü]{2,18}$", value):
            raise ValueError("Votre nom n'est pas valide")
        return str.__new__(cls, value.title())