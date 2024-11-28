#Job13

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    
NL = []

for i in L:
    if i not in NL:
        NL.append(i)
print("Liste sans doublons:", NL)