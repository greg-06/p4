import datetime


def from_birthdate_to_age(born):
    # calcul l'âge à partir de la date
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))