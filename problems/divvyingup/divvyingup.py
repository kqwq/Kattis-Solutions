n=int(input())
c = sum(list(map(int, input().split())))
if c % 3 == 0:
  print("yes")
else:
  print("no")