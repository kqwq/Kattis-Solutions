import math


n = int(input())
sum=0

for i in range(n):
    a, b, c = map(int, input().split())
    cosB = (a**2 + c**2 - b**2) / (2 * c * a)
    B = math.acos(cosB)
    
    cx = -a + (c/2) * math.cos(B)
    cy = (c/2) * math.sin(B)
    theta = math.atan(cy / cx)
    F = abs(c * math.sin(theta - B))
    sum += F 
print(sum)