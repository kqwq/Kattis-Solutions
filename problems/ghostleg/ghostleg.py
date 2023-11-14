

n, m = map(int, input().split())
rungs = []

for i in range(m):
  rungs.append(int(input()))

for i in range(n):
  pos = i + 1
  for j in range(m-1, -1, -1):
    if pos == rungs[j]:
      pos += 1
    elif pos == rungs[j] + 1:
      pos -= 1
  print(pos)
