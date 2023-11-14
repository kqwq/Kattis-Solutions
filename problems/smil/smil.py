
pos = []
smiles = [":)", ";)", ":-)", ";-)"]
s = input()

for smile in smiles:
    sLen = len(smile)
    for i in range(len(s) - sLen + 1):
        sub = s[i:i+sLen]
        if sub == smile:
            pos.append(i)

pos.sort()
for p in pos:
    print(p)