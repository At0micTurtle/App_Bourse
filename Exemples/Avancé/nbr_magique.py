import random

MIN = 1
MAX = 100
nbr_magique = random.randint(MIN, MAX)

def deviner_nombre(n):
    if n > nbr_magique:
        print("Le nombre magique est plus petit")
        return -1
    elif n < nbr_magique:
        print("Le nombre magique est plus grand")
        return 1
    else:
        print("Bravo, vous avez trouvé le nombre magique")
        return 0
    
min = MIN
max = MAX
def demander_nombre_ai(r, last_n):
    global min, max
    if r == 0:
        return last_n
    if r == 1:
        min = last_n + 1
    
    if r == -1:
        max = last_n - 1

    if min == max:
        return min
    
    if max - min == 1:
        if min == last_n:
            return max
        else:
            return min

    return (min+max)//2 # représente une division entière

print("Le nombre magique est: ", nbr_magique)
print()

n = 5
print("Je teste avec:", n)
r = deviner_nombre(n)
print()

while(r != 0):
    n = demander_nombre_ai(r, n)
    print("Je teste avec:", n)
    r = deviner_nombre(n)
    print()
    if r == 0:
        break