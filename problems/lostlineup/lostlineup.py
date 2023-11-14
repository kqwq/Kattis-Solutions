n = int(input())

lineup = [0] * n
lineup[0] = 1
d = map(int, input().split())

for k, v in enumerate(d):
  lineup[v + 1] = k + 2

print(*lineup)
