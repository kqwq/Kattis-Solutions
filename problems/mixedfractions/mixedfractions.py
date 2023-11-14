

while 1:
  a, b = map(int, input().split())
  if a == 0:
    break

  c = a // b
  a -= c * b
  print(c, a, "/", b)