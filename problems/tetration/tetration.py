


n = float(input())

ch = 1
while ch > 0.000001:
  n2 = n ** (1/n)
  ch = n2 - n
  n = n2

print(n)