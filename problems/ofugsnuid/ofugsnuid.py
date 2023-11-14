n = int(input())

lines = []
for i in range(n):
  lines.append(input())
for i in range(n-1, -1, -1):
  print(lines[i])