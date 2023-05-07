# --- Définition de la classe ---
class Personne:
    """
    __init__ est important pour la création d'une classe.
    C'est le constructeur de la classe.
    
    Le self représente l'instance de la classe.
    Il est obligatoire dans les méthodes de la classe.
    """
    def __init__(self, prenom: str = "", age: int = 0):
        # Création d'une variable d'instance
        self.prenom = prenom
        self.age = age
        if prenom == "":
            self.DemanderPrenom()
        print("Constructeur de la classe Personne " + self.prenom)
    
    def SePresenter(self):
        info_personne = "Bonjour, je m'appelle " + self.prenom + "."
        if self.age != 0:
            info_personne += " J'ai " + str(self.age) + " ans."
        print(info_personne)

        if self.age != 0:
            print("Je suis majeur." if self.EstMajeur() else "Je suis mineur.")
        print()

    def EstMajeur(self):
        return self.age >= 18
    
    def DemanderPrenom(self):
        self.prenom = input("Quel est votre prénom? ")

# --- Utilisation de la classe ---
personne1 = Personne("Jean", 15)
personne2 = Personne("Paul", 30)

personne3 = Personne()
personne4 = Personne()

print()

personne1.SePresenter()
personne2.SePresenter()
personne3.SePresenter()
personne4.SePresenter()

print()

print("Nom1: " + personne1.prenom + ", Age1: " + str(personne1.age) + ", Majeur1: " + str(personne1.EstMajeur()))
print("Nom2: " + personne2.prenom + ", Age2: " + str(personne2.age) + ", Majeur2: " + str(personne2.EstMajeur()))
