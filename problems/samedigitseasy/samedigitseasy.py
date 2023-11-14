a, b = map(int, input().split())

li = []

for x in range(a, b):
  for y in range(x, b+1):
    digitsXY = list(str(x)) + list(str(y))
    digitsXY.sort()
    product = x * y
    digitsProduct = list(str(product))
    digitsProduct.sort()
    if len(digitsXY) == len(digitsProduct):
      foundDifference = False
      for i in range(len(digitsXY)):
        if digitsXY[i] != digitsProduct[i]:
          foundDifference = True
          break
      if not foundDifference:
        li.append([x, y, product])

print("{} digit-preserving pair(s)".format(len(li)))
for item in li:
  print("x = {}, y = {}, xy = {}".format(item[0], item[1], item[2]))