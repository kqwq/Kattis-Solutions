

t = int(input())
for testCase in range(t):
  n = int(input())
  w = []
  for i in range(n):
    wTotal = sum(map(int, input().split()[1:]))
    w.append(wTotal)
  w.sort()
  timeAccum = 0
  timeTotal = 0
  for ww in w:
    timeAccum += ww
    timeTotal += timeAccum
  print(timeTotal / n)