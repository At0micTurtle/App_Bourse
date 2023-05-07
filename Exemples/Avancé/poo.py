# --- Classe parent ---
class EtreVivant:
    ESPECE = "Être vivant non identifié"

    def __init__(self):
        print("Constructeur de la classe EtreVivant")
        print()

    def AffichierEspece(self):
        print("Espèce:", self.ESPECE)

# --- Classes enfants ---
class Chat(EtreVivant): # Héritage de la classe EtreVivant
    ESPECE = "Chat (Mammifère félin)"

    def __init__(self):
        print("Constructeur de la classe Chat")
        print()

# --- Classe enfant ---
class Personne(EtreVivant):
    # Création d'une variable de classe.
    # Elle est partagée par toutes les instances de la classe et
    # peut être appelé soit par la classe (Personne.espece) ou par une instance de la classe (self.espece).
    ESPECE = "Humain (Mammifère homosapien)"
    
    #__init__ est le constructeur de la classe. Il est appelé lors de la création d'une instance de la classe.
    def __init__(self, prenom: str = "", age: int = 0):
        # Création d'une variable d'instance
        self.prenom = prenom
        self.age = age
        if prenom == "":
            self.DemanderPrenom()
        print("Constructeur de la personne " + self.prenom)
        print()
    
    def SePresenter(self):
        info_personne = "Bonjour, je m'appelle " + self.prenom + "."
        if self.age != 0:
            info_personne += " J'ai " + str(self.age) + " ans."
        print(info_personne)

        if self.age != 0:
            print("Je suis majeur." if self.EstMajeur() else "Je suis mineur.")

    def EstMajeur(self):
        return self.age >= 18
    
    def DemanderPrenom(self):
        self.prenom = input("Quel est votre prénom? ")

class Etudiant(Personne):
    def __init__(self, prenom: str, age: int, etudes: str):
        # Super() permet d'appeler le constructeur de la classe parent
        super().__init__(prenom, age)
        self.etudes = etudes

    def SePresenter(self):
        super().SePresenter()
        print("J'étudie en " + self.etudes + ".")

# --- Utilisation de la classe Personne---

liste_personnes = [Personne("Jean", 15),
                   Personne("Paul", 30),
                   Personne("Marie", 20)]

for personne in liste_personnes:
    personne.SePresenter()
    personne.AffichierEspece()
    print()

# --- Utilisation de la classe Etudiant ---
etudiant = Etudiant("Jean", 20, "Informatique")
etudiant.SePresenter()
etudiant.AffichierEspece()
print()

# --- Utilisation de la classe Chat ---
chat = Chat()
chat.AffichierEspece()
print()

# --- Utilisation de la classe EtreVivant ---
etreVivant = EtreVivant()
etreVivant.AffichierEspece()
