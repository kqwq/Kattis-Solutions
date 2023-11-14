pos = 1

s = input()
for c in s:
    if c == "A" and pos != 3:
        pos = 3 - pos
    elif c == "B" and pos != 1:
        pos = 5 - pos
    elif c == "C" and pos != 2:
        pos = 4 - pos
print(pos)