import json
from typing import Any
from pydantic.types import PositiveInt


"""le fichier manager est destiné à implémenter
le crud = create read update delete
(permet de communiquer avec la base de données)"""

""" work in progress => charger un tournoi complet
avec ses tours et matchs """


class Manager:
    """on gère une collection d'entités chargés
    à partir d'une source de données (json):
    charger un fichier json
    créer une entité (joueur ou tournoi)
    pouvoir retrouver une entité via son identifiant
    pouvoir récupérer la liste des entités"""
    def __init__(self, items_type: Any) -> None:
        self.items = {}
        self.items_type = items_type

    def read(self):
        return list(self.items.values())

    def read_by_id(self, id: PositiveInt):
        return self.items[id]

    def load_json_from_file(self, path: str):
        with open(path) as read_file:
            json_data = json.load(read_file)
            for data in json_data:
                self.create(data)

    def create(self, data):
        item = self.items_type(**data)  # ** opérateur de décompactage nommé
        self.items[item.id] = item
        return item
