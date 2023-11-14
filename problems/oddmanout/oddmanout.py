


n = int(input())

for i in range(n):
  guests = int(input())
  counts = {}
  codes = [int(c) for c in input().split()]
  for code in codes:
    if code in counts:
      counts[code] += 1
    else:
      counts[code] = 1
  for k, v in counts.items():
    if v == 1:
      print("Case #" + str(i+1) + ":", k)
      break