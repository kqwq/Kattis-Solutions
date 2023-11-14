

def sumDigits(x):
  return sum(map(int, list(str(x))))

while 1:
  n = int(input())
  if n == 0:
    quit()
  nSumDigits = sumDigits(n)

  p = 11
  while 1:
    if nSumDigits == sumDigits(p * n):
      print(p)
      break
    p += 1