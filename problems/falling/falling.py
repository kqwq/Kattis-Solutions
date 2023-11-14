d = int(input())

# 2 pointer solution
a = 0
b = 1
while a != b:
  val = b**2 - a**2
  if val < d:
    b += 1
  elif val > d:
    a += 1
  else:
    print(a,b)
    quit()
print("impossible")