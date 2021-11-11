
from typing import Any, Dict, List, Tuple
import os
import time
import sys
from models.player import Player
from models.tournament import Tournament
from termcolor import cprint


def scroll_text(text):
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    input()
    os.system("cls")


# Classe mère
class View:
    def __init__(self, title: str, message: str, error: str = "", blocking: bool = False):
        self.title = title
        self.message = message
        self.error = error
        self.blocking = blocking

    def display(self):
        os.system("cls")  # TD : rendre compatible unix
        print(f"{bcolors.HEADER}={bcolors.ENDC}" * 50 + "\n" + self.title + "\n" + f"{bcolors.HEADER}={bcolors.ENDC}" * 50 + "\n" + self.message + "\n" + f"{bcolors.HEADER}─{bcolors.ENDC}" * 50)
        if self.error:
            input(self.error)
        if self.blocking:
            print(f"{bcolors.HEADER}Appuyez sur <Entrée> pour continuer...{bcolors.ENDC}")
            input()


class ResumeMenu(View):
    def __init__(self):
        super().__init__(f"{bcolors.HEADER}💤  waiting for resume 💤{bcolors.ENDC}" + "\n\n" + "Press <Enter> to resume... ", "")

    def display(self):
        os.system("cls")
        cprint(f"{self.title}" + "\n" + f"{self.message}")


# Classe fille
class Menu(View):
    def __init__(self, title: str, options: List[Tuple[str, Any]]):
        """"""
        message = "\n".join([f"{nb}: {option}" for nb, (option, _) in enumerate(options, start=1)])
        View.__init__(self, title, message)
        self.options = options

    def display(self):
        """"""
        super().display()
        while True:
            try:
                choice = int(input(f"{bcolors.OKGREEN}👉  Choisissez votre option entre 1 et {len(self.options)} :{bcolors.ENDC}  "))
                # one_option = int(input(""))
                if 0 < choice <= len(self.options):
                    return self.options[choice - 1][1]
                else:
                    print("Entrez une option valide")
            except ValueError:
                pass


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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
                os.system("cls")
                super().display()
                try:
                    self.data[field_name] = field_type(input(field_desc + " : "))
                    self.error = ""
                    self.message = self.template.format(**self.data)
                    break
                except ValueError:
                    self.error = f"{bcolors.HEADER}Saisie incorrecte, appuyez sur <Entrée>...{bcolors.ENDC}" + "\n"
        super().display()

        input()

        return self.data


class ListView(View):
    def __init__(self, title: str, items: List[Any]):
        super().__init__(title=f"{title}", message="\n".join([str(item) for item in items]), blocking=True)
        # super().__init__(title=title, message="\n".join([item.render_players(12) for item in items])


# ListView(title="list", items=[]).display()

class PlayerAddForm(Form):
    """"""
    def __init__(self):
        """"""
        super().__init__(title=f"{bcolors.BOLD}🧾 Fiche joueur{bcolors.ENDC}", template=PLAYER_DICT, fields={
            "first_name": (f"{bcolors.OKGREEN}Nom du joueur{bcolors.ENDC}", str),
            "last_name": (f"{bcolors.OKGREEN}Prénom du joueur{bcolors.ENDC}", str),
            "birthdate_year": (f"{bcolors.OKGREEN}Année de naissance du joueur{bcolors.ENDC}", int),
            "birthdate_month": (f"{bcolors.OKGREEN}Mois de naissance du joueur{bcolors.ENDC}", int),
            "birthdate_day": (f"{bcolors.OKGREEN}Jour de naissance du joueur{bcolors.ENDC}", int),
            "gender": (f"{bcolors.OKGREEN}Sexe{bcolors.ENDC}", str),
            "rank": (f"{bcolors.OKGREEN}Classement du joueur{bcolors.ENDC}", int)
        })


class TournamentAddForm(Form):
    def __init__(self):
        """"""
        super().__init__(title="🧾 Fiche tournoi", template=TOURNAMENT_DICT, fields={
            "name": (f"{bcolors.OKGREEN}Nom du tournoi{bcolors.ENDC}", str),
            "place": (f"{bcolors.OKGREEN}Lieu du tournoi{bcolors.ENDC}", str),
            "nb_turns": (f"{bcolors.OKGREEN}Nombre de tours", int),
            "nb_players": (f"{bcolors.OKGREEN}Nombre de participants{bcolors.ENDC}", int)
            })


class ManagePlayerMenu(Menu):
    def __init__(self):
        """"""
        super().__init__(f"{bcolors.BOLD}🧾 Manage players menu{bcolors.ENDC}",
                         [
                             ("New player", "/New player"),
                             ("List players by name", "/List players by name"),
                             ("List players by rank", "/List players by rank"),
                             ("Edit player rank", "/Edit player rank"),
                             ("Back", "/Back")
                             ]
                         )


class MainMenu(Menu):
    def __init__(self):
        """"""
        super().__init__(f"{bcolors.BOLD}📌 Menu principal{bcolors.ENDC}",
                         [
                             ("Manage tournaments", "/tournaments"),
                             ("Manage players", "/players"),
                             ("Quit the program", "/quit")
                             ]
                         )


class ManageTournament(Menu):
    def __init__(self):
        """"""
        super().__init__(f"{bcolors.BOLD}🧾 Manage tournaments menu{bcolors.ENDC}",
                         [
                             ("Create tournament", "/create tournament"),
                             ("List tournaments", "/list tournaments"),
                             ("Resume tournament", "/resume tournament"),
                             ("Back", "/back")])


class CreateTournamentMenu(Menu):
    def __init__(self):
        """"""
        super().__init__(f"{bcolors.BOLD}🧾 Create tournament{bcolors.ENDC}",
                         [
                             ("Name", "/Name"),
                             ("Place", "/Place"),
                             ("Date", "/Date"),
                             ("Tours Number", "/Tours Number"),
                             ("Description", "/Description"),
                             ("Time Control", "/Time Control"),
                             ("Back", "/Back")
                             ]
                         )


class ListTournamentsMenu(ListView):
    def __init__(self, tournaments: List[Tournament]):
        super().__init__(f"{bcolors.BOLD}🧾 List tournaments{bcolors.ENDC}", [str(tournament.render_tournaments(52, ".")) for tournament in tournaments])


class ListPlayersByNameMenu(ListView):
    def __init__(self, players: List[Player]):
        super().__init__(f"{bcolors.BOLD}🧾 List player by name menu{bcolors.ENDC}", [str(player.render_players(18)) for player in players])


class ListPlayersByRankMenu(ListView):
    def __init__(self, players: List[Player]):
        super().__init__(f"{bcolors.BOLD}🧾 List player by rank menu{bcolors.ENDC}", [str(player.render_players(18)) for player in players])


class EditPlayerRankMenu(Form):
    def __init__(self, players: List[Player]):
        pass
