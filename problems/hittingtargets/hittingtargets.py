
m = int(input())
c = []
r = []
for i in range(m):
  line = input().split()
  if line[0] == "rectangle":
    r.append(list(map(int, line[1:])))
  else:
    c.append(list(map(int, line[1:])))


n = int(input())
for i in range(n):
  shots = 0
  x, y = map(int, input().split())
  for rr in r:
    if x >= rr[0] and x <= rr[2] and y >= rr[1] and y <= rr[3]:
      shots += 1
  for cc in c:
    if ((cc[0] - x)**2 + (cc[1] - y)**2)**0.5 <= cc[2]:
      shots += 1
  print(shots)