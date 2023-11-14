n=int(input())
for i in range(n):
  k = int(input())
  n = 0
  for steps in range(k):
    n = n * 2 + 1
  print(n)
  