import math

h,k,v,s=map(int,input().split())


x  = 0
while h > 0:
    v += s
    v -= max(1, math.floor(v / 10))
    if v >= k:
        h += 1
    if 0 < v and v < k:
        h -= 1
        if h == 0:
            v = 0
    if v <= 0:
        h = 0
        v = 0
    x += v
    if s > 0:
        s -= 1

print(x)