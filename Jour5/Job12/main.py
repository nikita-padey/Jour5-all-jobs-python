#Job12

L = [7, 11, 42, 39, 2]

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