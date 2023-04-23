# Les types de variables

# age = "30" -> type str
# age = 30 -> type int
# prix = 30.5 -> type float
# age = True/False -> type bool
# age = None -> type NoneType
# str(30) -> Convertir un nombre en chaîne de caractères
# int(age) -> Convertir une chaîne de caractères en nombre entier

"""
Commentaires
sur
plusieurs
lignes
"""

nom = input("Quel est ton nom? ") # Représente une chaîne de caractères
rep_age = input("Quel est ton âge? ")
age = 0 # Initialisation de la variable age

# Gestion d'erreur
try:
    age = int(rep_age)
except:
    print("Erreur: Vous devez rentrer un nombre pour l'âge.")
else:
    print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans.")
    print("L'an prochain, vous aurez " + str(age+1) + " ans.")

print("") # Saut de ligne

# Validation de données
nom = ""
while nom == "":
    nom = input("Quel est ton nom? ")
    if nom == "":
        print("Erreur: Vous devez rentrer un nom.")

age = 0
while age == 0:
    rep_age = input("Quel est ton âge? ")
    try:
        age = int(rep_age)
    except:
        print("Erreur: Vous devez rentrer un nombre pour l'âge.")
    else:
        print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans.")
        print("L'an prochain, vous aurez " + str(age+1) + " ans.")

print("") # Saut de ligne

# Boucle while
n = 0 # Initialisation de la variable n

# while condition:
while n < 10: # Tant que n est inférieur à 10
    # instructions
    print(n) # Afficher la valeur de n
    n += 1 # Incrémenter la valeur de n de 1

print("") # Saut de ligne

mot_de_passe = "1234" # Mot de passe à trouver
tentative = "" # Initialisation de la variable tentative

# while condition:
while mot_de_passe != tentative: # Tant que le mot de passe n'est pas trouvé
    # instructions
    tentative = input("Quel est le mot de passe? ") # Demander le mot de passe

print("Mot de passe trouvé!") # Afficher le message de réussite

print("") # Saut de ligne

# Boucle for

# for variable in range(0, 10):
for i in range(10): # Pour i allant de 0 à 9
    # instructions
    print(i) # Afficher la valeur de i

print("") # Saut de ligne

# for i in range(0, 10, 2): # Pour i allant de 0 à 9 par pas de 2
for i in range(0, 10, 2): # Pour i allant de 0 à 9 par pas de 2. Ici, 0 est inclus et 10 est exclu
    # instructions
    print(i) # Afficher la valeur de i

print("") # Saut de ligne

# for i in range(10, 0, -1): # Pour i allant de 10 à 1 par pas de -1
for i in range(10, 0, -1): # Pour i allant de 10 à 1 par pas de -1. Ici, 10 est inclus et 0 est exclu
    # instructions
    print(i) # Afficher la valeur de i

print("") # Saut de ligne

# Boucle for avec une chaîne de caractères
mot = "Bonjour" # Initialisation de la variable mot

# for variable in mot:
for lettre in mot: # Pour chaque lettre dans le mot
    # instructions
    print(lettre) # Afficher la lettre

print("") # Saut de ligne

# Boucle for avec une liste
liste = ["Bonjour", "à", "tous"] # Initialisation de la variable liste

# for variable in liste:
for mot in liste: # Pour chaque mot dans la liste
    # instructions
    print(mot) # Afficher le mot

print("") # Saut de ligne

# Boucle for avec une liste de nombres
liste = [1, 2, 3, 4, 5] # Initialisation de la variable liste

# for variable in liste:
for nombre in liste: # Pour chaque nombre dans la liste
    # instructions
    print(nombre) # Afficher le nombre

print("") # Saut de ligne

