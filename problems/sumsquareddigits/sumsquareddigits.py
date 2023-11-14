p = int(input())



for i in range(p):
  k, b, n = map(int, input().split())
  total = 0

  digits = []
  while n > 0:
    val = n % b
    digits.append(val)
    n //= b
  
  for d in digits:
    total += d ** 2

  print(k, total)

