import math

n, w, h = map(int, input().split())
whMax = math.sqrt(w**2 + h**2)

for i in range(n):
    x = int(input())
    if x > whMax:
        print("NE")
    else:
        print("DA")