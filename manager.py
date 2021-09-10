import json
from models.player import Player


class Manager:
    """on gère une collection d'entités chargés à partir d'une source de données (json):
    charger un fichier json
    créer une entité (joueur ou tournoi)
    pouvoir retrouver une entité via son identifiant
    pouvoir récupérer la liste des entités"""
    def __init__(self) -> None:
        """attributs 
        d'instance 
        de class"""         
        pass
    
    def manage_players(self):
        with open("players.json", "w") as write_file:
            json.dump("players.json", write_file)

      
    