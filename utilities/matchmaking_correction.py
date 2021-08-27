from random import randint, choice

players = [
    {"id": 1, "rank": randint(1, 3000)},  # Ici on se rapproche de la structure
    {"id": 2, "rank": randint(1, 3000)},  # d'un véritable joueur
    {"id": 3, "rank": randint(1, 3000)},  # (pas de score en interne)
    {"id": 4, "rank": randint(1, 3000)},
    {"id": 5, "rank": randint(1, 3000)},
    {"id": 6, "rank": randint(1, 3000)},
    {"id": 7, "rank": randint(1, 3000)},
    {"id": 8, "rank": randint(1, 3000)}
]


def get_player_score(p_id, scores):
    """ Lecture du score d'un joueur """
    s = 0
    for (p1_id, s1), (p2_id, s2) in scores:
        if p_id == p1_id:
            s += s1
        elif p_id == p2_id:
            s += s2
    return s


def gen_round(round, players, tournament_matchups, tournament_scores):
    """ Génération du round """
    matchups = []
    if round == 1:
        players = sorted(players, key=lambda x: x["rank"])
        matchups = [
            gen_matchup(p1, p2) for p1, p2 in zip(players[:4], players[4:])]
        tournament_matchups += matchups
    else:
        round_players = sorted(
            players, key=lambda x: (
                -get_player_score(x["id"], tournament_scores), x["rank"]))
        while round_players:
            p1 = round_players.pop(0)
            match = search_matchup_and_remove_opponent(
                p1, round_players, tournament_matchups)
            if not match:
                match = gen_matchup(p1, round_players.pop(0))
            matchups.append(match)
            tournament_matchups.append(match)
    print(matchups)
    return matchups


def gen_score(match, randomized=True):
    """ Génération du score d'un match """
    score1 = choice((0, 0.5, 1)) if randomized \
        else float(input("Entrez un score: "))
    score2 = 1 - score1
    return ((match[0], score1), (match[1], score2))


def gen_matchup(p1, p2):
    """ Génèration d'un match """
    return (min(p1['id'], p2['id']), max(p1['id'], p2['id']))


def search_matchup_and_remove_opponent(p1, players, m):
    """ Recherche d'un matchup et suppression d'un opposant
        de la liste des joueurs qui doivent encore jouer """
    for p2 in players:
        matchup = gen_matchup(p1, p2)
        if matchup not in m:
            players.pop(players.index(p2))
            return matchup


def gen_tournament(nb_rounds=4):
    """ Génération d'un tournois """
    tournament_matchups = []
    tournament_scores = []
    for r in range(1, nb_rounds):
        matchups = gen_round(
            r, players, tournament_matchups, tournament_scores)
        tournament_scores += [gen_score(m) for m in matchups]
    return tournament_scores


if __name__ == "__main__":
    tournament_ranking = sorted(
        [(p["id"], get_player_score(
            p["id"], gen_tournament())) for p in players], key=lambda x: -x[1])
    print("\n".join(
        [f"#{k}: player {p_id} with a score of {float(score)}"
            for k, (p_id, score) in enumerate(tournament_ranking)]))
    print(tournament_ranking)