
n = int(input())
total = 0

for i in range(n):
  s = input()
  a = int(s[:-1])
  b = int(s[-1])
  total += a ** b


print(total)