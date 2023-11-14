
n = int(input())
t=0
for i in range(n):
  line = input().lower()
  if "pink" in line or "rose" in line:
    t += 1

if t == 0:
  print("I must watch Star Wars with my daughter")
else:
  print(t)