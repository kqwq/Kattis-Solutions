

v = 7
n = int(input())
for i in range(n):
  if "op" in input():
    v += 1
  else:
    v -= 1
  if v > 10:v=10
  if v < 0: v=0
print(v)