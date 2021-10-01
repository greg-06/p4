
from typing import List
from models.player import Player

# Classe mère
class View:
    def __init__(self, title: str, message: str):
        self.title = title
        self.message = message

    def display(self):
        print("=" * 50 + "\n" + self.title + "\n" + "=" * 50 + "\n" + self.message + "\n" + "_" * 50 + "\n")


# View("Titre", "Message").display()

# Classe fille
class Menu(View):
    def __init__(self, title: str, options: List[str]):
        message = "\n".join([f"{nb}: {option}" for nb, option in enumerate(options, start=1)])
        View.__init__(self, title, message)
        self.options = options

    def display(self):
        super().display()
        while True:
            try:
                choice = int(input("Choisissez votre option : "))
                if 0 < choice < len(self.options):
                    return choice
                else:
                    print("Entrez une option valide")
            except ValueError:
                pass


''' créer une classe <formulaire> héritant de View,
    capable de demander à l'utilisateur de rentrer des champs
    et l'ensemble de ces champs sont retournés par display en tant que dictionnaire'''


PLAYER_DICT = """ID : <nombre entier>
Classement : <entre 1000 et 2000>
Nom : <nom>
Prénom : <prénom>
Date de naissance : <YYYY-MM-DD>
Sexe : <M> ou <F>"""

player_dict_model = {
        "id": "",
        "rank": "",
        "first_name": "",
        "last_name": "",
        "birthdate": "",
        "gender": ""
    }

nb_champs = len(player_dict_model)


# for i in list(player_dict_model):
#     choice = input("Saisissez l'id du joueur : ")
#     player_dict_model["id"] = choice    
#     choice = input("Saisissez le classement du joueur : ")
#     player_dict_model["rank"] = choice
#     choice = input("Saisissez le nom du joueur : ")
#     player_dict_model["first_name"] = choice
#     choice = input("Saisissez le prénom du joueur : ")
#     player_dict_model["last_name"] = choice
#     choice = input("date de naissance : ")
#     player_dict_model["birthdate"] = choice
#     choice = input("Sexe : ")
#     player_dict_model["gender"] = choice                    
#     print(player_dict_model)
#     break


class Form(View):
    def __init_(self, title: str, message: str):
        View.__init__(self, title, message)

    def display(self):
        super().display()
        while True:
            try:
                if player_dict_model:                    
                    choice = input("Saisissez l'id du joueur : ")
                    player_dict_model["id"] = choice
                    choice = input("Saisissez le classement du joueur : ")
                    player_dict_model["rank"] = choice
                    choice = input("Saisissez le nom du joueur : ")
                    player_dict_model["first_name"] = choice
                    choice = input("Saisissez le prénom du joueur : ")
                    player_dict_model["last_name"] = choice
                    choice = input("date de naissance : ")
                    player_dict_model["birthdate"] = choice
                    choice = input("Sexe : ")
                    player_dict_model["gender"] = choice
                    print(player_dict_model)
                    return choice
            except ValueError:
                pass


formulaire = Form("Fiche joueur", str(PLAYER_DICT))
formulaire.display()

# main_menu = Menu("Main menu", ["Manage tournaments", "Manage players", "Quit the program"])
# main_menu.display()

# tournament_menu = Menu("Tournament Menu", ["Create", "List", "Resume1", "Back to main menu"])
# tournament_menu.display()

# players_menu = Menu("Players Menu", ["By name", "By rank", "Player rank", "Back to Main menu"])
# players_menu.display()
