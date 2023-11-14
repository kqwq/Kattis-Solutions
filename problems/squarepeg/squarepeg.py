l, r = map(int, input().split())

if l < r * 2 / 2 ** 0.5:
  print("fits")
else:
  print("nope")