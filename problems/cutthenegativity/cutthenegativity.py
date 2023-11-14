n = int(input())
lines = []

for i in range(n):
    row = input().split()
    j = 0
    for cell in row:
        if int(cell) > 0: lines.append([i+1, j+1, cell])
        j += 1

print(len(lines))
for line in lines:
    print(*line)