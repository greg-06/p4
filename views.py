class View:
    """affiche un titre et un message"""
    def __init__(self, title, message):
        self.title = title
        self.message = message

    def display(self):
        print("=====" + "\n" + self.title + "\n" + "=====" + "\n" + self.message)


class Menu(View):
    def __init__(self):
        super().__init__(self)
        self.view = "view"


View("Titre", "Message").display()

""" créer une classe menu qui hérite de la classe view. Rajouter l'input.
Héritage et métaclasses à voir, iso 8601 à voir également. """
