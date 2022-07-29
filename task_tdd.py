
list_town = ['Paris', 'Budapest', 'Skopje', 'Rotterdam', 'Valence', 'Vancouver', 'Amsterdam', 'Vienne', 'Sydney', 'New York', 'Londres', 'Bangkok', 'Hong Kong', 'Dubaï', 'Rome', 'Istanbul']


def search_word(choix):
    for val in list_town:
        if choix == '*' and len(choix) < 2:
            return [list_town]
            break
        elif len(choix) >= 2 and choix.upper() in val.upper():
            return [val]
        elif len(choix) < 2:
            return "nothing to show"
            break
