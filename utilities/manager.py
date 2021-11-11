import json
from typing import Any
from pydantic.types import PositiveInt
from tinydb import TinyDB
from tinydb.table import Document


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
        self.max_id = 0
        self.load_database()

    def read(self):
        return list(self.items.values())

    def read_by_id(self, id: PositiveInt):
        return self.items[id]

    def create(self, data, save: bool = False):
        if "id" not in data:
            data["id"] = self.max_id + 1
        item = self.items_type(**data)  # ** opérateur de décompactage nommé
        self.items[item.id] = item
        self.max_id = max(self.max_id, item.id)
        if save:
            self.save_item(item.id)
        return item

    def load_database(self):
        database = TinyDB("database.json")
        self.table = database.table(self.items_type.__name__.lower() + "s")
        for itemdata in self.table:
            self.create(itemdata)

    def save_item(self, id: PositiveInt):
        item = self.read_by_id(id)
        self.table.upsert(Document(json.loads(item.json()), doc_id=id))

# créer une fonction pour sauvegarder les données
