n, v, h = map(int,input().split())

vol = 4 * max(v, n-v) * max(h, n-h)
print(vol)