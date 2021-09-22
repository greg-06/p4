from managers import tournament_manager, player_manager


def main():
    """"""
    tournament_manager.load_json_from_file("JSON/tournaments.json")
    player_manager.load_json_from_file("JSON/players.json")


if __name__ == "__main__":
    main()
