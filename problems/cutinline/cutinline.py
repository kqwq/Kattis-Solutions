n = int(input())

names = []
for i in range(n):
  names.append(input())

c = int(input())
for i in range(c):
  line = input()
  if line.count(" ") == 1:
    line += " _"
  action, a, b = line.split()
  if action == "cut":
    if a in names:
      names.remove(a)
    for (j, name) in enumerate(names):
      if b == name:
        names.insert(j, a)
        break
  elif action == "leave":
    names.remove(a)

for name in names:
  print(name)
