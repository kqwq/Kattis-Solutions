

while True:
  n = int(input())
  if n == 0:
    quit()
  x = []
  for i in range(2*n):
    x.append(int(input()))
  mid = len(x) // 2
  p1 = x[:mid]
  p2 = x[mid:]
  sortedP1 = sorted(p1)
  sortedP2 = sorted(p2)
  for p in p1:
    corro = sortedP2[sortedP1.index(p)]
    print(corro)
  print()