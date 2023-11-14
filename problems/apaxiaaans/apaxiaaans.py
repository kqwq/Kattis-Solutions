
a = input()
ss = ""
lastChar = ""
for i in range(len(a)):
    char = a[i]
    if char != lastChar:
        ss += char
    lastChar = char
print(ss)