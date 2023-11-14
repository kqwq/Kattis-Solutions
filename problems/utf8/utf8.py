
n = int(input())

types = [0, 0, 0, 0] # 1 to 4
left = 0
for i in range(n):
  line = input()

  if left == 0:
    typ = 0
    if line.startswith("0"):
      typ = 1
      left = 1
    elif line.startswith("110"):
      typ = 2
      left = 2
    elif line.startswith("1110"):
      typ = 3
      left = 3
    elif line.startswith("11110"):
      typ = 4
      left = 4
    else:
      print("invalid")
      quit()
    types[typ-1] += 1

  else:
    if not line.startswith("10"):
      print("invalid")
      quit()

  left -= 1

if left != 0:
  print('invalid')
  quit()

for typ in types:
  print(typ)

  