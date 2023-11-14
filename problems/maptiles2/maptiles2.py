
n = input()

zoom = len(n)

x = 0
y = 0
for i in range(zoom):
  digit = n[i]
  if digit == "1" or digit == "3":
    x += 2 ** (zoom - i - 1)
  if digit == "2" or digit == "3":
    y += 2 ** (zoom - i - 1)
print(zoom, x, y)



