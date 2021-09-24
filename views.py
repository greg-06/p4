
class View:
    """affiche un titre et un message"""
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def display(self):
        print("=" * 50 + "\n" + self.title + "\n" + "=" * 50 + "\n" + self.message + "\n" + "_" * 50 + "\n")


# View("Titre", "Message").display()


class Menu(View):
    def __init__(self, title, message, menu):
        super().__init__(title, message)
        self.menu = menu

    def display(self):
        print("=" * 50 + "\n" + self.title + "\n" + "=" * 50)
        print(self.message)
        print("-" * 50 + " \n" + self.menu + "\n" + "-" * 50 + "\n")


view = View("Main Menu", "Choisissez votre option : ")
view.display()

menu1 = Menu("Nom du Menu", "Choisissez votre option", "[1] Manage tournaments\n[2] Manage players\n[3] Quit the program")
menu1.display()


MAIN_MENU_CHOICES = ["1", "2", "3"]

OPTIONS_MAIN_MENU = """1 Manage tournaments
2 Manage players
3 Quit the program"""

View("Main menu", OPTIONS_MAIN_MENU).display()

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
