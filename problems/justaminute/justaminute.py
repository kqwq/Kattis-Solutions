

n = int(input())

mm = 0
ss = 0
for i in range(n):
  m, s = map(int, input().split())
  mm += m
  ss += s

slMinute = ss / mm / 60
if slMinute <= 1:
  print("measurement error")
else:
  print(slMinute)

