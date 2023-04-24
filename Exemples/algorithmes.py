# Tri par sélection

print("Tri par sélection")

def generate_random_list(n, min, max):
    import random
    l = []
    for i in range(n):
        e = random.randint(min, max)
        l.append(e)
    return l

def selection_sort(l):
    for unsorted_index in range(0, len(l)-1):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        l[min_index] = l[unsorted_index]
        l[unsorted_index] = min

l = generate_random_list(10, 0, 100)
print("Liste non triée:", l)

selection_sort(l)
print("Liste triée:", l)

print()

# Tri à bulle
print("Tri à bulle")

def bubble_sort(l):
    for i in range(len(l)-1, 0, -1):
        for j in range(0, i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp

l = generate_random_list(10, 0, 100)

print("Liste non triée:", l)

bubble_sort(l)
print("Liste triée:", l)

print()

# Tri rapide
print("Tri rapide")

def quick_sort(l):
    if len(l) < 2:
        return l
    pivot = l[0]
    left = []
    right = []
    for i in range(1, len(l)):
        if l[i] < pivot:
            left.append(l[i])
        else:
            right.append(l[i])
    return quick_sort(left) + [pivot] + quick_sort(right)

l = generate_random_list(10, 0, 100)

print("Liste non triée:", l)

l = quick_sort(l)
print("Liste triée:", l)

print()

# linear search
print("Recherche linéaire")

def linear_search(l, e):
    for i in range(len(l)):
        if l[i] == e:
            return i
    return -1

l = generate_random_list(10, 0, 100)

print("Liste:", l)

e = int(input("Entrez un nombre à rechercher: "))
index = linear_search(l, e)
if index == -1:
    print("Le nombre n'est pas dans la liste")
else:
    print("Le nombre est à l'index", index)

print()

# dichotomic search
print("Recherche dichotomique")

def dichotomic_search(l, e):
    left = 0
    right = len(l)-1
    while left <= right:
        middle = (left + right) // 2
        if l[middle] == e:
            return middle
        elif l[middle] < e:
            left = middle + 1
        else:
            right = middle - 1
    return -1

l = generate_random_list(10, 0, 100)
l.sort()

print("Liste:", l)

e = int(input("Entrez un nombre à rechercher: "))
index = dichotomic_search(l, e)
if index == -1:
    print("Le nombre n'est pas dans la liste")
else:
    print("Le nombre est à l'index", index)

print()

# binary search
print("Recherche binaire")

def binary_search(l, e):
    left = 0
    right = len(l)-1
    while left <= right:
        middle = (left + right) // 2
        if l[middle] == e:
            return middle
        elif l[middle] < e:
            left = middle + 1
        else:
            right = middle - 1
    return -1

l = generate_random_list(10, 0, 100)
l.sort()

print("Liste:", l)

e = int(input("Entrez un nombre à rechercher: "))
index = binary_search(l, e)
if index == -1:
    print("Le nombre n'est pas dans la liste")
else:
    print("Le nombre est à l'index", index)

print()
