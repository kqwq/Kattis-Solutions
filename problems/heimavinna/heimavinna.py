

parts = input().split(";")
count = 0
for part in parts:
  if "-" in part:
    s,e=map(int, part.split("-"))
    count += e-s+1
  else:
    count += 1
print(count)