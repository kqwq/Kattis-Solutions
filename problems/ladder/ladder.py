import math

h, v = map(int, input().split())

vRadians = v * math.pi / 180

print(math.ceil(h /math.sin(vRadians)))