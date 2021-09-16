import json
from typing import Any
from pydantic.types import PositiveInt
from models.player import Player
from models.tournament import Tournament

"""le fichier manager est destiné à implémenter
le crud = create read update delete
(permet de communiquer avec la base de données)"""

""" work in progress => charger un tournoi complet
avec ses tours et matchs """


class Manage_player:
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


class Manage_tournoi:
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
    

player_list_json = Manage_player(Player)
player_list_json.load_json_from_file("JSON/players.json")
print(player_list_json.items)

tournament_list_json = Manage_tournoi(Tournament)
tournament_list_json.load_json_from_file("JSON/tournaments.json")
print(tournament_list_json)

