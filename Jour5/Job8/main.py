#Job8


L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

add = []

for i in L:
    if i % 2 == 0:
        add.append(i)


somme = sum(add)
print("la somme des nombre paire de la liste L est",somme)