
lines = []
for i in range(5):
  lines.append(input())

a = []
for i in range(5):
  if "FBI" in lines[i]:
    a.append(i+1)

if len(a) == 0:
  print("HE GOT AWAY!")
else:
  b = map(str, a)
  print(" ".join(b))