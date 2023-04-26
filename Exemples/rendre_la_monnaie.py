"""
Rendre la monnaie
Glouton (greedy) | Brute force

121$
50, 20, 10, 5, 2, 1
2 x 50
1 x 20
1 x 1

121$
50, 20, 10, 5, 2
2 x 50
1 x 20
...
2 x 50
3 x 5
3 x 2
"""

def cash_back_greedy(s, e):
    
    r = []

    for a in e:
        r.append(s // a)
        s = s % a

    for i in range(len(e)):
        if r[i] > 0:
            print(r[i], 'x', e[i])

    if s > 0:
        print("Reste de:", s)
    else:
        print("Toute la monnaie a été rendue")

    return r

def cash_back_brute_force(s, e):
    
    results = []
    c = [0] * len(e)

    while(c[0] * e[0] <= s):        
        v = sum([c[i] * e[i] for i in range(len(e))])
        
        if v == s:
            results.append((c.copy(), sum(c)))
            print("Solution trouvée:", c)

        c[-1] += 1

        i = len(e) - 1
        while(v > s):
            c[i] = 0
            c[i-1] += 1
            v = sum([c[i] * e[i] for i in range(len(e))])
            print("sup", c, "->", v)
            i -= 1
            if i == 0:
                break

    print("END")
    results.sort(key=lambda x: x[1], reverse=True)
    for r in results:
        print(r)

#print(cash_back_greedy(121, [50, 20, 10, 5, 2, 1]))
print(cash_back_brute_force(121, [50, 20, 10, 5, 2, 1]))