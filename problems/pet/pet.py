con = []
bestI = 0
best = 0
for i in range(5):
    a,b,c,d=map(int, input().split())
    tot = a+b+c+d
    if tot > best:
        best = tot
        bestI = i
print(bestI + 1, best)