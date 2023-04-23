# Exemple de fonctions
def demander_nom():
    """ Demande le nom de l'utilisateur et le renvoie. """
    nom = ""
    while nom == "":
        nom = input("Quel est ton nom? ")
        if nom == "":
            print("Erreur: Vous devez rentrer un nom.")

def demander_age():
    """ Demande l'âge de l'utilisateur et le renvoie. """
    age = 0
    while age == 0:
        rep_age = input("Quel est ton âge? ")
        try:
            age = int(rep_age)
        except:
            print("Erreur: Vous devez rentrer un nombre pour l'âge.")

nom = demander_nom()
age = demander_age()

print("")

""" Affiche les informations de l'utilisateur. """
print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans.")
print("L'an prochain, vous aurez " + str(age+1) + " ans.")

# Exemple de fonctions avec paramètres
def demander_nom():
    """ Demande le nom de l'utilisateur et le renvoie. """
    nom = ""
    while nom == "":
        print("")
        nom = input("Quel est ton nom? ")        
        if nom == "":
            print("Erreur: Vous devez rentrer un nom.")

    return nom

def demander_age(nom_utilisateur):
    """ Demande l'âge de l'utilisateur et le renvoie. """
    age = 0
    while age == 0:
        print("")
        rep_age = input(nom_utilisateur + ", quel est ton âge? ")
        try:
            age = int(rep_age)
        except:
            print("Erreur: Vous devez rentrer un nombre pour l'âge.")

    return age

def afficher_infos(nom, age):
    """ Affiche les informations de l'utilisateur. """
    print("")
    print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans.")
    print("L'an prochain, vous aurez " + str(age+1) + " ans.")

    # == egal
    # != différent
    # < inférieur
    # > supérieur
    # <= inférieur ou égal
    # >= supérieur ou égal
    
    # Affiche si l'utilisateur est majeur ou mineur
    if age >= 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes mineur.")

nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

""" Affiche les informations des l'utilisateurs. """
afficher_infos(nom1, age1)

afficher_infos(nom2, age2)

# Exemple elif
def demander_nom():
    """ Demande le nom de l'utilisateur et le renvoie. """
    nom = ""
    while nom == "":
        print("")
        nom = input("Quel est ton nom? ")        
        if nom == "":
            print("Erreur: Vous devez rentrer un nom.")

    return nom

def demander_age(nom_utilisateur):
    """ Demande l'âge de l'utilisateur et le renvoie. """
    age = 0
    while age == 0:
        print("")
        rep_age = input(nom_utilisateur + ", quel est ton âge? ")
        try:
            age = int(rep_age)
        except:
            print("Erreur: Vous devez rentrer un nombre pour l'âge.")

    return age

def afficher_infos(nom, age):
    """ Affiche les informations de l'utilisateur. """
    print("")
    print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans.")
    # print(f"Vous vous appelez {nom} et vous avez {age} ans.")
    #print("Vous vous appelez %s et vous avez %s ans." % (nom, age))
    
    print("L'an prochain, vous aurez " + str(age+1) + " ans.")
    # print("L'an prochain, vous aurez %s ans." % (age+1))    

    # En Python, le mot-clé elif est la contraction de else if
    if age == 17:
        print("Vous êtes presque majeur.")
    elif age >= 12 and age < 18: # façon simplifiée -> 12 <= age < 18
        print("Vous êtes un adolescent.")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé.")
    elif age == 18:
        print("Vous êtes tout juste majeur. Félicitations!")
    elif age > 18:
        print("Vous êtes majeur.")
    else:
        print("Vous êtes un enfant.")

nom1 = demander_nom()
nom2 = demander_nom()

age1 = demander_age(nom1)
age2 = demander_age(nom2)

""" Affiche les informations des l'utilisateurs. """
afficher_infos(nom1, age1)

afficher_infos(nom2, age2)
