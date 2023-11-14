v = int(input())

n = int(input())

for i in range(n):
  city, c = input().split()
  cur = int(c)
  if v <= cur:
    print(city, "opin")
  else:
    print(city, "lokud")

