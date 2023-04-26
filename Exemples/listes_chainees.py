"""
Liste chainée :
Une liste chainée est composée de cellules mémoires, chacune contenant un élément et un pointeur vers la cellule suivante.
La liste chainée est donc une structure de données dynamique, contrairement aux tableaux qui sont statiques.

Les opérations de base sur une liste chainée sont :
- Création d'une liste chainée
- Insertion d'un élément dans une liste chainée
- Suppression d'un élément dans une liste chainée
- Recherche d'un élément dans une liste chainée
- Affichage d'une liste chainée
- Destruction d'une liste chainée

Node (Noeud) : une cellule mémoire d'une liste chainée
Head (Tête) : le premier noeud d'une liste chainée
Tail (Queue) : le dernier noeud d'une liste chainée

Data (Donnée) : l'élément contenu dans une cellule mémoire
Next (Suivant) : le pointeur vers la cellule suivante
"""

# Création d'une liste chainée
class LinkedList:
    def __init__(self, head):
        self.head = head

    def get_nb_nodes(self):
        node = self.head
        nb_nodes = 0
        while node is not None:
            nb_nodes += 1
            node = node.next
        return nb_nodes
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def set_next(self, next):
        self.next = next

node1 = Node("Bonjour") # Head
node2 = Node("tout")
node3 = Node("le")
node4 = Node("monde") # Tail

node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)

linked_list = LinkedList(node1)
print("Nombre de noeuds:", linked_list.get_nb_nodes())

# Affichage d'une liste chainée
def print_list(head):
    node = head
    while node is not None:
        print(node.data)
        node = node.next

print_list(node1)

# Insertion d'un élément dans une liste chainée
