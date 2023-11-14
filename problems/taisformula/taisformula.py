n = int(input())


totalArea = 0
t, v = map(float, input().split())
for i in range(n-1):
  tLast = t
  vLast = v
  t, v = map(float, input().split())

  area = (min(v, vLast) + abs(v - vLast) / 2) * (t - tLast) / 1000
  totalArea += area

print(totalArea)

