
hash = set()

s = input()
for c in s:
    if c in hash:
        print(0)
        quit()
    hash.add(c)
print(1)