
while 1:
  n = int(input())
  if n == -1:
    quit()
  
  tot = 0
  lastB = 0
  for i in range(n):
    a, b = map(int, input().split())
    tot += a * (b - lastB)
    lastB = b
  print(tot, "miles")
