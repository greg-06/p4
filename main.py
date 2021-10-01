from managers import tournament_manager, player_manager


def main():  # le main est le controleur
    """afficher un menu principal
    permettre à l'utilisateur de faire sa selecion
    et le rediriger vers le sous-menu (joeur, tournoi ou quitter)"""
    tournament_manager.load_json_from_file("JSON/tournaments.json")
    player_manager.load_json_from_file("JSON/players.json")


if __name__ == "__main__":
    main()
