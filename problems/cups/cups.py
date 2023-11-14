
n = int(input())

cups = []
for i in range(n):
  line = input()
  a, b = line.split()
  if a.upper() == a:
    cups.append([int(a) / 2, b])
  else:
    cups.append([int(b), a])
  
cups.sort(key=lambda x:x[0])

for c in cups:
  print(c[1])