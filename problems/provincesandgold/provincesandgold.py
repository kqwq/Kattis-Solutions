

buy = []
g, s, c = map(int, input().split())

bp = g * 3 + s * 2 + c

if bp >= 8:
  buy.append("Province")
elif bp >= 5:
  buy.append("Duchy")
elif bp >= 2:
  buy.append("Estate")

if bp >= 6:
  buy.append("Gold")
elif bp >= 3:
  buy.append("Silver")
else:
  buy.append("Copper")

print(" or ".join(buy))