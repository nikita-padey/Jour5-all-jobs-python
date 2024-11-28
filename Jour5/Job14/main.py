#Job14

def my_long_word(chiffre, chaine):
    mots = chaine.split()
    resultat = []

    for mot in mots:
        count = 0
        for char in mot:
            count += 1
        if count > chiffre:
            resultat.append(mot)

    return " ".join(resultat)

chaine = input("donne une phrase entre "": ")
print(my_long_word(3, chaine))
