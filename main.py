from managers import tournament_manager, player_manager
from views import CreateTournamentMenu, EditPlayerRankMenu, ListPlayersByNameMenu, ListPlayersByRankMenu, ListTournamentsMenu, MainMenu, ManagePlayerMenu, ManageTournament, NewPlayerMenu, ResumeTournamentMenu
import os


def manage_tournaments():
    """fonction qui affiche le menu de gestion des tournois
    redirige l'utilisateur vers le menu de l'option sélectionnée"""
    while True:
        choice = ManageTournament().display()
        if choice == 1:
            CreateTournamentMenu().display()
        elif choice == 2:
            ListTournamentsMenu().display()
        elif choice == 3:
            ResumeTournamentMenu().display()
        else:
            break


def manage_players_menu():
    """fonction qui affiche le menu de gestion des joueurs
    redirige l'utilisateur vers le menu de l'option sélectionnée"""
    while True:
        choice = ManagePlayerMenu().display()
        if choice == 1:
            NewPlayerMenu().display()
        elif choice == 2:
            ListPlayersByNameMenu().display()
        elif choice == 3:
            ListPlayersByRankMenu().display()
        elif choice == 4:
            EditPlayerRankMenu().display()
        else:
            break


def main():  # le main est le controleur
    """charge les fichiers json
    affiche le menu principal
    redirige l'utilisateur vers le menu de l'option sélectionnée
    permet à l'utilisateur de quitter le programme"""
    tournament_manager.load_json_from_file("JSON/tournaments.json")
    player_manager.load_json_from_file("JSON/players.json")

    while True:
        choice = MainMenu().display()
        if choice == 1:
            manage_tournaments()
        elif choice == 2:
            manage_players_menu()
        elif choice == 3:
            os.system("cls")
            print("🌈  Merci d'avoir utilisé ce programme, à bientôt !" + "\n")
            break


if __name__ == "__main__":
    main()
