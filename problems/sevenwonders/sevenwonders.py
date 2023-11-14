

s = input()

t = 0
g = 0
c = 0
for r in s:
  if r == "T":t+=1
  if r == "G":g+=1
  if r == "C":c+=1

m = min(t, g, c)
print(m * 7 + t ** 2 + g ** 2 + c ** 2)