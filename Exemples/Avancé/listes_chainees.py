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
    
    def get_all_data_as_list(self):
        node = self.head
        data = []
        while node is not None:
            data.append(node.data)
            node = node.next
        return data
    
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
print("Toutes les données:", linked_list.get_all_data_as_list())

print()

# Insertion d'un élément dans une liste chainée
def insert_node(linked_list, node, index):
    if index == 0:
        node.next = linked_list.head
        linked_list.head = node
    else:
        previous_node = linked_list.head
        for i in range(index-1):
            previous_node = previous_node.next
        node.next = previous_node.next
        previous_node.next = node

node5 = Node("Hello")
insert_node(linked_list, node5, 2)
print("Nombre de noeuds:", linked_list.get_nb_nodes())
print("Toutes les données:", linked_list.get_all_data_as_list())

print()

# Suppression d'un élément dans une liste chainée
def remove_node(linked_list, index):
    if index == 0:
        linked_list.head = linked_list.head.next
    else:
        previous_node = linked_list.head
        for i in range(index-1):
            previous_node = previous_node.next
        previous_node.next = previous_node.next.next

remove_node(linked_list, 2)
print("Nombre de noeuds:", linked_list.get_nb_nodes())
print("Toutes les données:", linked_list.get_all_data_as_list())

print()
