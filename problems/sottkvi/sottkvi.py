

n, k, d = map(int, input().split())
q = []
for i in range(n):
    q.append(int(input()))

makeIt = 0
for qq in q:
    if qq + 14 <= k + d:
        makeIt += 1

print(makeIt)
