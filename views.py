
class View:
    """affiche un titre et un message"""
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def display(self):
        print("=" * 50 + "\n" + self.title + "\n" + "=" * 50 + "\n" + self.message + "\n" + "_" * 50)


# View("Titre", "Message").display()


class Menu(View):
    def __init__(self, title, message, menu):
        super().__init__(title, message)
        self.menu = menu

    def display(self):
        print("Titre : " + self.title)
        print("Message : " + self.message)
        print("Menu : " + self.menu)


view = View("mon_titre", "mon_message")
view.display()

menu1 = Menu("titre_test", "message_test", "menu_test")
menu1.display()


# MAIN_MENU_CHOICES = ["1", "2", "3"]

# TEXTE_MAIN_MENU = """1 Manage tournaments
# 2 Manage players
# 3 Quit the program"""

# View("Main menu", TEXTE_MAIN_MENU).display()

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
