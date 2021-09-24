
# Classe mère
from re import L
from typing import List


class View:
    def __init__(self, title, message):
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


class form(View):
    def __init__(self, title, message):
        super().__init__(title, message)
        

main_menu = Menu("Main menu", ["Manage tournaments", "Manage players", "Quit the program"])
main_menu.display()

tournament_menu = Menu("Tournament Menu", ["Create", "List", "Resume1", "Back to main menu"])
tournament_menu.display()

players_menu = Menu("Players Menu", ["By name", "By rank", "Player rank", "Back to Main menu"])
players_menu.display()




# form1 = form()
# form1.display()
'''créer class form (formulaire) doit retourner un dico'''



# menu = Menu("Nom du Menu", "Choisissez votre option", "[1] Manage tournaments\n[2] Manage players\n[3] Quit the program")
# menu.display()


# MAIN_MENU_CHOICES = ["1", "2", "3"]

# OPTIONS_MAIN_MENU = """1 Manage tournaments
# 2 Manage players
# 3 Quit the program"""

# View("Main menu", OPTIONS_MAIN_MENU).display()

""" créer une classe menu qui hérite de la classe view.
Héritage et métaclasses à voir, iso 8601 à voir également. """

# while MAIN_MENU_CHOICES != 3:
#     user_choice = ""
#     if user_choice == "1":
#         print("")
#     if user_choice == "1":
#         print("")
#     elif user_choice == "3":
#         sys.exit()
#     print("Thanks for using this program. Goodbye !")
