"""
Supprimer les doublons

1 - Comparaison linéaire (n²)
2 - Comparaison par tri (n log n)
3 - Comparaison par hachage (n)

exists
set
"""

from tools import generate_random_list

l = generate_random_list(20, 0, 10)
print("Avant comparaisons:", l)

print()

# 1 - Comparaison linéaire (n²)
def remove_duplicates1(l):
    r = []
    for e in l:
        if e not in r:
            r.append(e)
    return r

print("Après comparaison linéaire:", remove_duplicates1(l))

print()

# 2 - Comparaison par tri (n log n)
def remove_duplicates2(l):
    l = sorted(l)
    r = []
    for i in range(len(l)):
        if i == 0 or l[i] != l[i-1]:
            r.append(l[i])
    return r

print("Après comparaison par tri:", remove_duplicates2(l))

print()

# 3 - Comparaison par hachage (n)
def remove_duplicates3(l):
    r = []
    s = set()
    for e in l:
        if e not in s:
            r.append(e)
            s.add(e)
    return r

print("Après comparaison par hachage:", remove_duplicates3(l))
