# Fonction pour générer une liste aléatoire de n entiers compris entre min et max
def generate_random_list(n, min, max):
    import random
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l