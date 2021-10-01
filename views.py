
from typing import Dict, List


# Classe mère
class View:
    def __init__(self, title: str, message: str):
        self.title = title
        self.message = message

    def display(self):
        print("=" * 50 + "\n" + self.title + "\n" + "=" * 50 + "\n" + self.message + "\n" + "=" * 50)


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


PLAYER_DICT = """ID : <nombre entier>
Classement : <entre 1000 et 2000>
Nom : <nom>
Prénom : <prénom>
Date de naissance : <YYYY-MM-DD>
Sexe : <M> ou <F>"""


class Form(View):
    def __init__(self, title: str, message: str, fields: Dict[str, str]):
        View.__init__(self, title, message)
        self.fields = fields

    def display(self):
        data = {}
        super().display()
        for field_name, field_desc in self.fields.items():
            data[field_name] = input(field_desc + " : ")
        return data


class PlayerAddForm(Form):
    def __init__(self):
        super().__init__(title="Fiche joueur", message=PLAYER_DICT, fields={
            "id": "Id du joueur",
            "rank": "Classement du joueur",
            "first_name": "Nom du joueur",
            "last_name": "Prénom du joueur",
            "birthdate": "Date de naissance",
            "gender": "Sexe"
        })


test = PlayerAddForm()
print(test.display())


# formulaire = Form("Fiche joueur", str(PLAYER_DICT))
# formulaire.display()

# main_menu = Menu("Main menu", ["Manage tournaments", "Manage players", "Quit the program"])
# main_menu.display()

# tournament_menu = Menu("Tournament Menu", ["Create", "List", "Resume1", "Back to main menu"])
# tournament_menu.display()

# players_menu = Menu("Players Menu", ["By name", "By rank", "Player rank", "Back to Main menu"])
# players_menu.display()
