import math

N = int(input())
for i in range(N):
  n, l, d, g = map(int, input().split())
  expansion = d * g

  areaEdge = l * expansion
  areaCorner = math.pi * expansion ** 2 / n

  a = l / 2 / math.tan(math.radians(180*(1/n)))
  p = l * n
  originalArea = a * p / 2
  area = (areaEdge + areaCorner) * n
  print(originalArea+area)

