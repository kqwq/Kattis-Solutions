from math import dist

x, y, x1, y1, x2, y2 = map(int, input().split())
p = (x, y)
p1 = (x1, y1)
p2 = (x1, y2)
p3 = (x2, y1)
p4 = (x2, y2)
a = 0

if x < x1:
  if y < y1:
    a = dist(p, p1)
  elif y > y2:
    a = dist(p, p2)
  else:
    a = x1 - x
elif x > x2:
  if y < y1:
    a = dist(p, p3)
  elif y > y2:
    a = dist(p, p4)
  else:
    a = x - x2
else:
  if y < y1:
    a = y1 - y
  elif y > y2:
    a = y - y2
  else:
    a = 0/0
print(float(a))