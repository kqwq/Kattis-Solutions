


n = int(input())


for i in range(0, 10_000):
  n -= (i*2+1) ** 2
  if n < 0:
    print(i)
    break