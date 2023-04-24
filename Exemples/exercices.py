# Inverser une chaîne de caractères
print("Inverser une chaîne de caractères")
def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -1):
        reversed_string += string[i]
    return reversed_string
    # return string[::-1] -> Autre méthode plus rapide s'il y a beaucoup de données

print(reverse_string("Bonjour toto"))

print()

# Compter les majuscules dans une chaîne de caractères
print("Compter les majuscules dans une chaîne de caractères")
def count_uppercase(string):
    l = [i for i in string if i.isupper()]
    return len(l)

print(count_uppercase("Bonjour Toto"))

print()

# Compter le nombre de voyelles dans une chaîne de caractères
print("Compter le nombre de voyelles dans une chaîne de caractères")
def count_vowels(string):
    vowels = "aeiouy"
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

print(count_vowels("Bonjour toto"))

print()

# Trouver le mot le plus cours et le plus long dans une chaîne de caractères
print("Trouver le mot le plus cours dans une chaîne de caractères")
def get_min_and_max_words(string):
    words = string.split(" ")
    min_word = words[0]
    max_word = words[0]
    for word in words:
        if len(word) < len(min_word):
            min_word = word
        if len(word) > len(max_word):
            max_word = word
    return min_word, max_word

phrase = "Un chasseur sachant chasser sans son chien est un bon chasseur"
min_word, max_word = get_min_and_max_words(phrase)
print("Phrase:", phrase)
print("Mot le plus court:", min_word)
print("Mot le plus long:", max_word)

print()

# Supprimer les doublons
print("Supprimer les doublons")
noms = ["Jean", "Marc", "Pierre", "Paul", "Jacques", "Marie", "Lucie", "Jean", "Marc", "Pierre", "Paul", "Jacques", "Marie", "Lucie"]
set_noms = list(set(noms)) # Convertir un set en liste
print(set_noms)

print()

# Mots communs entre deux phrases
print("Mots communs entre deux phrases")

string1 = "Bonjour tout le monde"
string2 = "Bonjour tout le monde et bienvenue"

def get_common_words(string1, string2):
    words1 = string1.split(" ")
    words2 = string2.split(" ")
    common_words = []
    for word in words1:
        if word in words2:
            common_words.append(word)
    return common_words

print(get_common_words(string1, string2))

print()

# Trouver les nombres pairs et impairs dans une liste
print("Trouver les nombres pairs et impairs dans une liste")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_even_and_odd_numbers(numbers):
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers

even_numbers, odd_numbers = get_even_and_odd_numbers(numbers)
print("Nombres pairs:", even_numbers)
print("Nombres impairs:", odd_numbers)

print()

# Trouver les nombres premiers dans une liste
print("Trouver les nombres premiers dans une liste")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False 
    return True

def get_prime_numbers(numbers):
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

print(get_prime_numbers(numbers))

print()

# Trouver les nombres premiers entre deux nombres
print("Trouver les nombres premiers entre 1 et 100")
def get_prime_numbers_between(min, max):
    prime_numbers = []
    for number in range(min, max + 1):
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers

print(get_prime_numbers_between(1, 100))

print()

# Données monotones
print("Données monotones")

def is_monotonic(numbers):
    if len(numbers) < 2:
        return True
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            return False
    return True

print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(is_monotonic([1, 2, 3, 4, 5, 6, 7, 8, 9, 8]))

print()

# Trouver les éléments manquants
print("Trouver les éléments manquants")

a = [2, 3, 5, 8]
def get_missing_elements(numbers):
    missing_elements = []
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] > 1:
            for j in range(numbers[i - 1] + 1, numbers[i]):
                missing_elements.append(j)
    return missing_elements

def get_missing_elements2(l, min, max):
    missing_elements = []
    for i in range(min, max + 1):
        if i not in l:
            missing_elements.append(i)
    return missing_elements

print(get_missing_elements([1, 4, 5, 8, 9]))
print(get_missing_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]))
print(get_missing_elements2(a, 1, 10))

print()
