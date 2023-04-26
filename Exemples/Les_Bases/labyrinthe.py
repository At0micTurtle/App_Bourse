"""
Labyrinthe
Tableaux à deux dimensions
Récursivité
Recherche de chemin

0 = mur
1 = chemin
-1 = chemin déjà emprunté
8 = entrée
9 = sortie
"""

# x = 0  1  2  3  4  5     y
m = [[8, 1, 1, 1, 1, 0],  # 0
     [1, 0, 1, 0, 1, 0],  # 1
     [1, 0, 0, 1, 1, 1],  # 2
     [1, 0, 0, 0, 1, 0],  # 3
     [1, 1, 1, 0, 1, 0],  # 4
     [0, 1, 0, 0, 1, 9]]  # 5

def find_maxe_exit(m, x, y):

    print("Exploring at:", x, y)

    if m[y][x] == 9:
        print("Maze exit found at:", x, y)
        for l in m:
            d = ""
            for e in l:
                if e == -1:
                    d += str(e) + " "
                else:
                    d += " " + str(e) + " "
            print(d)
        exit(0)

    m[y][x] = -1

    # On explore à gauche
    if x > 0: 
        if m[y][x-1] >= 1:
            find_maxe_exit(m, x-1, y)

    # On explore à droite
    if x < len(m[0])-1:
        if m[y][x+1] >= 1:
            find_maxe_exit(m, x+1, y)
    
    # On explore en haut
    if y > 0: 
        if m[y-1][x] >= 1:
            find_maxe_exit(m, x, y-1)

    # On explore en bas
    if y < len(m)-1:
        if m[y+1][x] >= 1:
            find_maxe_exit(m, x, y+1)

find_maxe_exit(m, 0, 0)