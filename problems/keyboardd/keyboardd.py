



i = 0

good = input()+" "
bad = input()+" "
sticky = set()

for g in good:
  while bad[i] != g:
    sticky.add(bad[i])
    i += 1
  i += 1

print("".join(list(sticky)))
