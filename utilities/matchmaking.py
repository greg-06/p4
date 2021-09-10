

def gen_matchup(p1, p2):
    """ Génèration d'une rencontre
    retourne une paire ordonnée d'identifiants des deux joueurs du match"""
    return tuple(sorted((p1['id'], p2['id'])))


def get_player_score(p_id, scores):
    '''Lecture du score d'un joueur
        on recherche un joueur dans la liste des scores 
        et si on le trouve on incrémente son score
    on retourne le score total'''
    s = 0
    for (p1_id, s1), (p2_id, s2) in scores:
        if p_id == p1_id:
            s += s1
        elif p_id == p2_id:
            s += s2
    return s


def gen_round(round, players, tournament_matchups, tournament_scores):
    """Génération du round :
    si il s'agit du premier round
        on trie les joueurs par classement
        on sépare les joueurs en 2 groupes
        on génère des matchs avec des paires consituées des joueurs du premier et deuxième groupe
        on met à jour la liste des matchs du tournoi
        on retourne la liste des matchs générés
    sinon
        on trie les joueurs par score et si ils sont équivalents on les trie par rang
        tant qu'il reste des joueurs qui n'ont pas joué
            on extrait un premier joueur
            on récupère son adversaire
            on génère le match
            on rajoute le match à la liste des matchups
            on met à jour la liste des matchs du tournoi
        on retourne la liste des matchs générés"""
    matchups = []
    if round == 1:
        players = sorted(players, key=lambda x: -x["rank"])
        matchups = [
            gen_matchup(p1, p2) for p1, p2 in zip(players[:4], players[4:])]
        tournament_matchups += matchups
    else:
        round_players = sorted(
            players, key=lambda x: (
                -get_player_score(x["id"], tournament_scores), -x["rank"]))
        while round_players:
            p1 = round_players.pop(0)
            p2 = search_opponent(
                p1, round_players, tournament_matchups)
            match = gen_matchup(p1, p2)
            matchups.append(match)
            tournament_matchups.append(match)
    print(matchups)
    return matchups


def gen_score(matchup):
    '''génère le score d'un match
       le score du joueur 1 est demandé à l'utilisateur
       le score du joueur 2 est déduit du score du joueur 1
    retourne un match joué sous la forme d'un tuple de deux tuples'''
    s1 = float(input("Entrez un score: "))
    s2 = 1 - s1
    return ((matchup[0], s1), ((matchup[1], s2)))


def search_opponent(p1, players, played_matchups):
    """Recherche d'un adversaire dans les joueurs restant du tour
    si le match a déjà été joué, on prend le joueur suivant
    si tous les matchs ont déjà été joués on prend le joueur ayant le meilleur score"""
    for p2 in players:
        matchup = gen_matchup(p1, p2)
        if matchup not in played_matchups:
            players.pop(players.index(p2))
            return p2
    return players.pop(0)


def gen_tournament(players, nb_rounds=4):
    """Génération d'un tournoi de 4 tours par défaut
    pour les N tours d'un tournoi
        on génère le tour (les matchups)
        puis on génère les scores du tour
    et on retourne les scores du tournoi"""
    tournament_matchups = []
    tournament_scores = []
    for r in range(1, nb_rounds + 1):
        matchups = gen_round(r, players, tournament_matchups, tournament_scores)
        tournament_scores += [gen_score(m) for m in matchups]
    return tournament_scores
