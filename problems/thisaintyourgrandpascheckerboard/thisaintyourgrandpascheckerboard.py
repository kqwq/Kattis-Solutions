n = int(input())

grid = []
for i in range(n):
  grid.append(input())

#rows and 3s
for line in grid:
  if line.count('W') != line.count("B") or "WWW" in line or "BBB" in line:
    print(0)
    quit()

for i in range(n):
  line = ""
  for j in range(n):
    line += grid[j][i]
  
  if line.count('W') != line.count("B") or "WWW" in line or "BBB" in line:
    print(0)
    quit()

print(1)