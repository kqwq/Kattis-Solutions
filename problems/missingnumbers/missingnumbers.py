
h = set()
n = int(input())
for i in range(n):
  n = int(input())
  h.add(n)

ma = max(h)
found = False
for i in range(1, ma+1):
  if i not in h:
    found = True
    print(i)

if not found:
  print("good job")