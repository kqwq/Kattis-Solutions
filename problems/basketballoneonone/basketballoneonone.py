

a = 0
b = 0

line = input()
for i in range(0, len(line), 2):
  letter = line[i]
  amount = int(line[i+1])

  if letter == "A":
    a += amount
  else:
    b += amount

if a > b:
  print('A')
else:
  print('B')