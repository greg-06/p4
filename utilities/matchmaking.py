from random import randint, choice

players = [
    {"id": 1, "rank": randint(1, 3000)},
    {"id": 2, "rank": randint(1, 3000)},
    {"id": 3, "rank": randint(1, 3000)},
    {"id": 4, "rank": randint(1, 3000)},
    {"id": 5, "rank": randint(1, 3000)},
    {"id": 6, "rank": randint(1, 3000)},
    {"id": 7, "rank": randint(1, 3000)},
    {"id": 8, "rank": randint(1, 3000)}
]


def get_player_score(p_id, scores):
    '''Lecture du score d'un joueur'''
    s = 0
    for (p1_id, s1), (p2_id, s2) in scores:
        if p_id == p1_id:
            s += s1
        elif p_id == p2_id:
            s += s2
    return s


def gen_first_round_matchups(players):
    '''Génère les 4 matchups du tour 1 (système Suisse)'''
    players.sort(key=lambda x: x["rank"])
    g1, g2 = players[:4], players[4:]  # slicing
    return [gen_matchup(g1[i], g2[i]) for i in range(4)]


def gen_score_matchup(matchup):
    '''Génère le score d'un match'''
    player1_id = matchup[0]
    player2_id = matchup[-1]
    s1 = choice((0, 0.5, 1))
    s2 = 1 - s1
    return ((player1_id, s1), (player2_id, s2))


def gen_matchup(p1, p2):
    '''Génère un match'''
    return f"{min(p1['id'], p2['id'])} vs {max(p1['id'], p2['id'])}"


'''Print des 4 matchups du tour 1'''
matchups_tour1 = gen_first_round_matchups(players)
print(matchups_tour1)


# def gen_score(match, randomized=True):
#     '''génère le score d'un match'''
#     s1 = choice((0, 0.5, 1)) if randomized \
#         else float(input("Entrez un score: "))
#     s2 = 1 - s1
#     return ((match[0], s1), ((match[1], s2)))


# def update_players_scores(players, scores):
# """fonction qui génère le score d'un match"""
#     for (p1_id, s1), (p2_id, s2) in scores:
#         p1 = list(filter(lambda x: x["id"] == p1_id, players)).pop()
#         p2 = list(filter(lambda x: x["id"] == p2_id, players)).pop()
#         p1["score"] += s1
#         p2["score"] += s2


# def find_opponent(p1, round_players, tournament_matchups):
#     '''trouve l'opposant d'un match'''
#     for p2 in round_players:
#         matchup = name_matchup(p1, p2)
#         if matchup not in tournament_matchups:
#             round_players.pop(round_players.index(p2))
#             return p2


# def gen_next_round_matchups(players, tournament_matchups):
#     """génère les rencontres suivantes"""
#     """find_opponet possiblement bogué"""
#     matchups = []
#     round_players = sorted(players, key=lambda x: (-x["score"], x["rank"]))
#     while round_players:
#         p1 = round_players.pop(0)
#         p2 = find_opponent(p1, round_players, tournament_matchups)
#         matchup = name_matchup(p1, p2)
#         matchups.append(matchup)
#         tournament_matchups.append(matchup)
#     return matchups


# tournament_matchups = []
# matchups_t1 = gen_first_round_matchups(players)
# tournament_matchups += matchups_t1
# scores_t1 = [score_matchup(matchup) for matchup in matchups_t1]

# # update_players_scores(players, scores_t1)
# gen_score(players, scores_t1)

# matchups_t2 = gen_next_round_matchups(players, tournament_matchups)
# tournament_matchups += matchups_t2
# scores_t2 = [score_matchup(matchup) for matchup in matchups_t2]

# # update_players_scores(players, scores_t2)
# gen_score(players, scores_t2)

# matchups_t3 = gen_next_round_matchups(players, tournament_matchups)
# tournament_matchups += matchups_t3
# scores_t3 = [score_matchup(matchup) for matchup in matchups_t3]

# # update_players_scores(players, scores_t3)
# gen_score(players, scores_t3)

# matchups_t4 = gen_next_round_matchups(players, tournament_matchups)
# tournament_matchups += matchups_t4
# scores_t4 = [score_matchup(matchup) for matchup in matchups_t4]

# # update_players_scores(players, scores_t4)
# gen_score(players, scores_t4)

# print(tournament_matchups)
# print(scores_t1, scores_t2, scores_t3, scores_t4)
