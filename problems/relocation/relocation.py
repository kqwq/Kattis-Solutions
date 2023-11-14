
n, q = map(int, input().split())

x = list(map(int, input().split()))

for i in range(q):
  # print(x, 888)
  typ, a, b = map(int, input().split())
  if typ == 1:
    x[a - 1] = b
  else:
    print(abs(x[a-1]-x[b-1]))
