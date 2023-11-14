

f, s, year = map(int, input().split("/"))

if f > 12:
  print("EU")
elif s > 12:
  print("US")
else:
  print("either")