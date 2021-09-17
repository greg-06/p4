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

""" créer une classe menu qui hérite de la classe view 
en utilisant au maximum ce que la classe view propose 
et en rajoutant input ce qui fait d'elle une classe parent.

héritage et métaclasses à voir """
