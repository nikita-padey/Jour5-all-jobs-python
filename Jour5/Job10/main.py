#Job10

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

add = []

for i in L:
    if 90 > i > 25:
        add.append(i)

somme = sum(add)
print("la somme des nombre paire de la liste L est",somme)