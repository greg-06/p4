
from typing import Dict, List
import os


# Classe mère
class View:
    def __init__(self, title: str, message: str):
        self.title = title
        self.message = message

    def display(self):
        os.system("cls")  # TD : rendre compatible unix
        print("=" * 50 + "\n" + self.title + "\n" + "=" * 50 + "\n" + self.message + "\n" + "=" * 50)


# Classe fille
class Menu(View):
    def __init__(self, title: str, options: List[str]):
        """"""
        message = "\n".join([f"{nb}: {option}" for nb, option in enumerate(options, start=1)])
        View.__init__(self, title, message)
        self.options = options

    def display(self):
        """"""
        super().display()
        while True:
            try:
                choice = int(input(f"👉  Choisissez votre option entre 1 et {len(self.options)} :  "))
                if 0 < choice <= len(self.options):
                    return choice
                else:
                    print("Entrez une option valide")
            except ValueError:
                pass


PLAYER_DICT = """ID : <nombre entier>
Classement : <entre 1000 et 2000>
Nom : <nom>
Prénom : <prénom>
Date de naissance : <YYYY-MM-DD>
Sexe : <M> ou <F>"""


TOURNAMENT_DICT = """ID : <nombre entier>,
Place: <ville>
Date_start: <YYYY-MM-DD>,
Date_end: <YYYY-MM-DD>,
Nb_turns (4 par défaut): <nombre entier>,
Players: <ID des joueurs>,
Turns: <liste des tours>"""


class Form(View):
    """"""
    def __init__(self, title: str, message: str, fields: Dict[str, str]):
        View.__init__(self, title, message)
        self.fields = fields

    def display(self):
        """"""
        data = {}
        super().display()
        for field_name, field_desc in self.fields.items():
            data[field_name] = input(field_desc + " : ")
        return data


class PlayerAddForm(Form):
    """"""
    def __init__(self):
        """"""
        super().__init__(title="Fiche joueur", message=PLAYER_DICT, fields={
            "first_name": "Nom du joueur",
            "last_name": "Prénom du joueur",
            "birthdate_year": "Année de naissance du joueur : ",
            "birthdate_month": "Moi de naissance du joueur : ",
            "birthdate_day": "Jour de naissance du joueur : ",
            "gender": "Sexe",
            "rank": "Classement du joueur"
        })


class TournamentAddForm(Form):
    def __init__(self):
        """"""
        super().__init__(title="Fiche tournoi", message=TOURNAMENT_DICT, fields={
            "name": "Nom du tournoi",
            "place": "Lieu du tournoi",
            "nb_turns": "Nombre tours",
            "nb_players": "Nombre de participants"
        })


class ManagePlayerMenu(Menu):
    def __init__(self):
        """"""
        super().__init__("🧾 Manage players menu", ["New player", "List players by name", "List players by rank", "Edit player rank", "Back"])


class MainMenu(Menu):
    def __init__(self):
        """"""
        super().__init__("📌 Menu principal", ["Manage tournaments", "Manage players", "Quit the program"])


class ManageTournament(Menu):
    def __init__(self):
        """"""
        super().__init__("🧾 Manage tournaments menu", ["Create tournament", "List tournaments", "Resume tournament", "Back"])


class CreateTournamentMenu(Menu):
    def __init__(self):
        """"""
        super().__init__("🧾 Create tournament", ["Name", "Place", "Date", "Tours Number", "Description", "Time Control", "Back"])


class ListTournamentsMenu(Menu):
    def __init__(self):
        super().__init__("🧾 List tournaments", ["Tournament1", "Tournament2", "Tournament3", "Back"])


class ResumeTournamentMenu(Menu):
    def __init__(self):
        super().__init__("🧾 Resume menu", ["Resume", "Back"])


class NewPlayerMenu(Menu):
    def __init__(self):
        super().__init__("🧾 New Player menu", ["First Name", "Last name", "Birthdate_year", "Birthdate_month", "Birthdate_day", "Gender", "Rank", "Back"])


class ListPlayersByNameMenu(Menu):
    def __init__(self):
        super().__init__("🧾 List player by name menu", ["player1", "player2", "player3", "player4", "player5", "player6", "player7", "player8", "back"])


class ListPlayersByRankMenu(Menu):
    def __init__(self):
        super().__init__("🧾 List player by rank menu", ["player1 rank", "player2 rank", "player3 rank", "player4 rank", "player5 rank", "player6 rank", "player7 rank", "player8 rank", "back"])


class EditPlayerRankMenu(Menu):
    def __init__(self):
        super().__init__("🧾 Edit player rank menu", ["Edit player_01 rank", "Edit player_02 rank", "Edit player_03 rank", "Edit player_04 rank", "Edit player_05 rank", "Edit player_06 rank", "Edit player_07 rank", "Edit player_08 rank", "back"])
