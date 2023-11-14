
l = int(input())
d = int(input())
x = int(input())

for i in range(l, d+1):
  sumDigits = sum(map(int, list(str(i))))
  if sumDigits == x:
    print(i)
    break
for i in range(d, l-1, -1):
  sumDigits = sum(map(int, list(str(i))))
  if sumDigits == x:
    print(i)
    break