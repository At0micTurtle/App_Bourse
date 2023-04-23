# Collections: Listes, tuples, tableaux, dictionnaires, slices, set
# Tuples (): immutable -> ne peut pas être modifié
# Liste []: mutable -> peut être modifié
# Tableaux : mutable -> peut être modifié
# Slice: mutable -> peut être modifié
# Dictionnaire {}: mutable -> peut être modifié
# Set: mutable -> peut être modifié

# Le tuple utilise moins de mémoire que la liste, donc plus rapide

# Exemple de tuple
print("Exemple de tuple")
personnes = ("Jean", "Marc", "Pierre", "Paul", "Jacques")
print(len(personnes))
print(personnes[-1]) # Affiche le dernier élément

for i in range(0, len(personnes)):
    print(personnes[i])

for i in personnes:
    print(i)
    print(len(i))
    print(i[0])

(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
valeurs = range(0, 10)
print(valeurs[-1])

print()

# Exemple de liste
print("Exemple de liste")
personnes = ["Jean", "Marc", "Pierre", "Paul", "Jacques"]
nouvelle_personne = "Marie"

print(personnes)

personnes.append(nouvelle_personne)
# personnes.extend(["Lucie", "Luc"]) -> Ajoute plusieurs éléments à la liste

print(personnes)

del personnes[0]

print(personnes)

personnes.remove("Marc")

print(personnes)

def afficher_personnes(personnes):
    for i in personnes:
        print(i)
    
afficher_personnes(personnes)

print()

# Exemple de Fonctions et tuples
print("Exemple de Fonctions et tuples")
def obtenir_information():
    nom = input("Entrez votre nom: ")
    prenom = input("Entrez votre prénom: ")
    age = input("Entrez votre âge: ")
    return nom, prenom, age

def afficher_information(nom, prenom, age):
    print("Nom: " + nom)
    print("Prénom: " + prenom)
    print("Age: " + age)

nom, prenom, age = obtenir_information()
afficher_information(nom, prenom, age)

print()

# Exemple de Slices
print("Exemple de Slices")
personnes = ["Jean", "Marc", "Pierre", "Paul", "Jacques"]
personnes.sort()
print(personnes)

print("fin sort")
print()

personnes.reverse()
print(personnes)

print("fin reverse")
print()

for i in personnes[0:3]: # Affiche les 3 premiers éléments. [start:stop:step] le step représente le pas
    print(i)

print()

# Liste algorithmique
print("Liste algorithmique")
nom_chaufeur = ["Jean", "Marc", "Pierre", "Paul", "Jacques", "Marie", "Lucie"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
noms_et_distances = [(nom_chaufeur[i], distance_chauffeur_km[i]) for i in range(len(nom_chaufeur))]
noms_et_distances.sort(key=lambda x: x[1])
print(noms_et_distances)

distance_min = distance_chauffeur_km[0]
for distance in distance_chauffeur_km:
    if distance < distance_min:
        distance_min = distance

print("Distance minimale:", distance_min, "km.", "Nom du chauffeur:", nom_chaufeur[distance_chauffeur_km.index(distance_min)])

print()

# Exercice questionnaire
print("Exercice questionnaire")
questionnaire = (
    ("Quelle est la capitale de la France?", ["Paris", "Lyon", "Marseille", "Toulouse" "Lille"], "Paris"),
    ("Quelle est la capitale de l'Italie?", ["Rome", "Milan", "Venise", "Turin"], "Rome"), 
    ("Quelle est la capitale de la Belgique?", ["Bruxelles", "Anvers", "Gand", "Charleroi"], "Bruxelles"))

def poser_question(question):
    choix = question[1]
    bonne_reponse = question[2]
    print("QUESTION:")
    print(" " + question[0])
    for i in range(len(choix)):
        print(" ", i+1, "-", choix[i])

    print()

    resultat_reponse = False
    reponse_int = demander_reponse(1, len(choix))
    if choix[reponse_int-1].lower() == bonne_reponse.lower():
        print("Bonne réponse!")
        resultat_reponse = True
    else:
        print("Mauvaise réponse!")

    print()
    return resultat_reponse

def demander_reponse(min, max):
    reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + "): ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        
        print("ERREUR: Vous devez entrer un nombr entre", min, "et", max)
    except:
        print("ERREUR: Veuillez entrer uniquement des chiffres.")
    return demander_reponse(min, max)    

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Votre score est de", score, "sur", len(questionnaire))

lancer_questionnaire(questionnaire)

print()

# Liste à 2 dimensions
print("Liste à 2 dimensions")
tableau = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in tableau:
    for j in i:
        print(j)

print()

for l in tableau:
    ligne = ""
    for c in l:
        ligne += str(c) + " "
    print(ligne)

print()

# Exemple de dictionnaire
print("Exemple de dictionnaire")

# clef -> valeur
p = {"nom": "Dupont", "prenom": "Jean", "age": 25}
print(p)
print(p["prenom"], p["nom"], p["age"]) # Affiche la valeur de la clef "nom". Si la clef n'existe pas, une erreur est retournée. print(p.get("nom")) -> Affiche None si la clef n'existe pas
print(p["prenom"])
print(p["age"])

repertoire = {"Jean Dupont": {"age": 25, "telephone": "418-123-4561"},
              "Marc Dupont": {"age": 30, "telephone": "418-123-4562"},
              "Pierre Dupont": {"age": 35, "telephone": "418-123-4563"},
              "Paul Dupont": {"age": 40, "telephone": "418-123-4564"},
}

for clef in repertoire:
    print(clef, ":", repertoire[clef]["telephone"])

print()

# Exemple de dictionnaire avec des fonctions
print("Exemple de dictionnaire avec des fonctions")

def afficher_personne(personne):
    print("Nom:", personne["nom"])
    print("Prénom:", personne["prenom"])
    print("Age:", personne["age"])

def obtenir_information():
    nom = input("Entrez votre nom: ")
    prenom = input("Entrez votre prénom: ")
    age = input("Entrez votre âge: ")
    return {"nom": nom, "prenom": prenom, "age": age}

def afficher_information(personne):
    print("Nom:", personne["nom"])
    print("Prénom:", personne["prenom"])
    print("Age:", personne["age"])

personne = obtenir_information()
afficher_information(personne)

print()

# Exemple de set. Utilisé pour enlever les doublons. Il n'y a pas d'ordre dans un set
print("Exemple de set")

noms = ["Jean", "Marc", "Pierre", "Paul", "Jacques", "Marie", "Lucie", "Jean", "Marc", "Pierre", "Paul", "Jacques", "Marie", "Lucie"]
set_noms = set(noms)
print(set_noms)

split_noms = "Jean,Marc,Pierre,Paul,Jacques,Marie,Lucie".split(",")
set_split_noms = set(split_noms)
print(set_split_noms)

join_noms = ",".join(set_split_noms)
print(join_noms)
