
from typing import Any, Dict, List, Tuple
import os

from models.player import Player


# Classe mère
class View:
    def __init__(self, title: str, message: str, error: str = "", blocking:bool = False):
        self.title = title
        self.message = message
        self.error = error
        self.blocking = blocking

    def display(self):
        os.system("cls")  # TD : rendre compatible unix
        print("=" * 50 + "\n" + self.title + "\n" + "=" * 50 + "\n" + self.message + "\n" + "=" * 50)
        if self.error:
            input(self.error)
        if self.blocking:
            input()


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


PLAYER_DICT = """Nom : {first_name}
Prénom : {last_name}
Date de naissance : {birthdate_year}-{birthdate_month}-{birthdate_day}
Sexe : {gender}
Classement : {rank}"""


TOURNAMENT_DICT = """Nom du tournoi : {name}
Lieu du tournoi : {place}
Nombre de tours : {nb_turns}
Nombre de participants : {nb_players}"""


class Form(View):
    """"""
    def __init__(self, title: str, template: str, fields: Dict[str, Tuple[str, Any]]):
        self.data = {k: "❔" for k in fields.keys()}  # dictio d'intention
        View.__init__(self, title, template.format(**self.data))  # opérateur de décompactage
        self.fields = fields
        self.template = template

    def display(self):
        """"""
        for field_name, (field_desc, field_type) in self.fields.items():
            while True:
                super().display()
                try:
                    self.data[field_name] = field_type(input(field_desc + " : "))
                    self.error = ""
                    self.message = self.template.format(**self.data)
                    break
                except ValueError:
                    self.error = "Saisie incorrecte, appuyez sur <Entrée>..." + "\n"
        super().display()

        input()

        return self.data


class PlayerAddForm(Form):
    """"""
    def __init__(self):
        """"""
        super().__init__(title="🧾 Fiche joueur", template=PLAYER_DICT, fields={
            "first_name": ("Nom du joueur", str),
            "last_name": ("Prénom du joueur", str),
            "birthdate_year": ("Année de naissance du joueur", int),
            "birthdate_month": ("Mois de naissance du joueur", int),
            "birthdate_day": ("Jour de naissance du joueur", int),
            "gender": ("Sexe", str),
            "rank": ("Classement du joueur", int)
        })


class TournamentAddForm(Form):
    def __init__(self):
        """"""
        super().__init__(title="🧾 Fiche tournoi", template=TOURNAMENT_DICT, fields={
            "name": ("Nom du tournoi", str),
            "place": ("Lieu du tournoi", str),
            "nb_turns": ("Nombre de tours", int),
            "nb_players": ("Nombre de participants", int)
            })


class ManagePlayerMenu(Menu):
    def __init__(self):
        """"""
        super().__init__("🧾 Manage players menu",
                         [
                             "New player",
                             "List players by name",
                             "List players by rank",
                             "Edit player rank",
                             "Back"
                             ]
                         )


class MainMenu(Menu):
    def __init__(self):
        """"""
        super().__init__("📌 Menu principal",
                         [
                             "Manage tournaments",
                             "Manage players",
                             "Quit the program"
                             ]
                         )


class ManageTournament(Menu):
    def __init__(self):
        """"""
        super().__init__("🧾 Manage tournaments menu",
                         [
                             "Create tournament",
                             "List tournaments",
                             "Resume tournament",
                             "Back"])


class CreateTournamentMenu(Menu):
    def __init__(self):
        """"""
        super().__init__("🧾 Create tournament",
                         [
                             "Name",
                             "Place",
                             "Date",
                             "Tours Number",
                             "Description",
                             "Time Control",
                             "Back"
                             ]
                         )


class ListTournamentsMenu(Menu):
    def __init__(self):
        super().__init__("🧾 List tournaments",
                         [
                             "Tournament1",
                             "Tournament2",
                             "Tournament3",
                             "Back"
                             ]
                         )


class ResumeTournamentMenu(Menu):
    def __init__(self):
        super().__init__("🧾 Resume menu",
                         [
                             "Resume",
                             "Back"
                             ]
                         )


class NewPlayerMenu(Menu):
    def __init__(self):
        super().__init__("🧾 New Player menu",
                         [
                             "First Name",
                             "Last name",
                             "Birthdate_year",
                             "Birthdate_month",
                             "Birthdate_day",
                             "Gender",
                             "Rank",
                             "Back"
                             ]
                         )


class ListPlayersByNameMenu(Menu):
    def __init__(self, players: List[Player]):
        super().__init__("🧾 List player by name menu", [str(player) for player in players])         



class ListPlayersByRankMenu(Menu):
    def __init__(self):
        super().__init__("🧾 List player by rank menu",
                         [
                             "player1 rank",
                             "player2 rank",
                             "player3 rank",
                             "player4 rank",
                             "player5 rank",
                             "player6 rank",
                             "player7 rank",
                             "player8 rank",
                             "back"
                             ]
                         )


class EditPlayerRankMenu(Menu):
    def __init__(self):
        super().__init__("🧾 Edit player rank menu",
                         [
                             "Edit player_01 rank",
                             "Edit player_02 rank",
                             "Edit player_03 rank",
                             "Edit player_04 rank",
                             "Edit player_05 rank",
                             "Edit player_06 rank",
                             "Edit player_07 rank",
                             "Edit player_08 rank",
                             "back"
                             ]
                         )

class ListView(View):
    def __init__(self, title, items: List[Any]):
        super().__init__(title=f"🧾 {title}", message="\n".join([str(item) for item in items]), blocking=True) 


ListView(title="list", items=[]).display()