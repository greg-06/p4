from managers import tournament_manager, player_manager
from views import (
    EditPlayerRankMenu,
    ListPlayersByNameMenu,
    ListPlayersByRankMenu,
    ListTournamentsMenu,
    MainMenu,
    ManagePlayerMenu,
    ManageTournament,
    ResumeMenu,
    PlayerAddForm,
    ResumeMenu,
    TournamentAddForm,
    bcolors,
    scroll_text
    )
import os


def manage_tournaments_controller():
    """fonction qui affiche le menu de gestion des tournois
    redirige l'utilisateur vers le menu de l'option sélectionnée"""
    choice = ManageTournament().display()
    if choice == "/create tournament":
        tournament_add_controller()
    elif choice == "/list tournaments":
        list_tournaments_controller()
    elif choice == "/resume tournament":
        resume_controller()
    elif choice == "/back":
        main_controller()


def manage_players_controller():
    """fonction qui affiche le menu de gestion des joueurs
    redirige l'utilisateur vers le menu de l'option sélectionnée"""
    choice = ManagePlayerMenu().display()
    if choice == "/New player":
        player_add_controller()
    elif choice == "/List players by name":
        list_players_by_name_controller()
    elif choice == "/List players by rank":
        list_players_by_rank_controller()
    elif choice == "/Edit player rank":
        edit_player_rank_controller()
    elif choice == "/Back":
        main_controller()


def main_controller():  # le main est le controleur
    """charge les fichiers json
    affiche le menu principal
    redirige l'utilisateur vers le menu de l'option sélectionnée
    permet à l'utilisateur de quitter le programme"""
    choice = MainMenu().display()
    if choice == "/tournaments":
        manage_tournaments_controller()
    elif choice == "/players":
        manage_players_controller()
    elif choice == "/quit":
        os.system("cls")
        print(scroll_text(f"{bcolors.OKCYAN}🌈  Merci d'avoir utilisé ce programme, à bientôt !{bcolors.ENDC}" + "\n" * 2 + "Press <Enter>... "))

        os.system("cls")


def tournament_add_controller():
    form_data = TournamentAddForm().display()
    input(form_data)
    manage_tournaments_controller()


def player_add_controller():
    form_data = PlayerAddForm().display()
    # form_data["birthdate"] = # compléter + créer un tournoi
    input(form_data)
    manage_players_controller()


def list_tournaments_controller():
    ListTournamentsMenu(tournament_manager.read()).display()
    manage_tournaments_controller()


def list_players_by_name_controller():
    ListPlayersByNameMenu(player_manager.read()).display()
    manage_players_controller()


def list_players_by_rank_controller():
    ListPlayersByRankMenu(player_manager.read()).display()
    manage_players_controller()


def edit_player_rank_controller():
    EditPlayerRankMenu(player_manager.read()).display()
    manage_players_controller()


def resume_controller():
    ResumeMenu().display()
    input()
    manage_tournaments_controller()


if __name__ == "__main__":
    main_controller()
