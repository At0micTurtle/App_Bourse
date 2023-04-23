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
