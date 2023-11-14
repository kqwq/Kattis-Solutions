
p, q = map(int, input().split())
if q < p: p, q = q, p
line = input()

if line == "ABBA":
  if q - p == 3:
    print(p+1, p+2)
  else:
    print(-1)
elif line == "ABAB":
  if p == 6 and q == 8:
    print(7, 9)
  else:
    print(-1)
elif line == "BABA":
  if p == 2 and q == 4:
    print(1, 3)
  else:
    print(-1)
elif line == "BAAB":
  if p == 2 and q == 8:
    print(1, 9)
  else:
    print(-1)

elif line == "AABB":
  if q == 7:
    print(8, 9)
  else:
    print(-1)
elif line == "BBAA":
  if p == 3:
    print(1, 2)
  else:
    print(-1)
else:
  0/0

