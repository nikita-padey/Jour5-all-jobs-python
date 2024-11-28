#Job15

X = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.60, 17.80]

L = []

for nombre in X:
    if nombre - int(nombre) >= 0.5:
        L.append(int(nombre) + 1)
    else:
        L.append(int(nombre))

done = False
while not done:
    done = True 
    i = 0 
    while i < 100:
        try:
            if L[i] > L[i + 1]: 
                L[i], L[i + 1] = L[i + 1], L[i]
                done = False
            i += 1
        except IndexError:
            break
print("Liste triée :", L)
