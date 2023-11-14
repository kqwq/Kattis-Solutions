

l, h = map(int, input().split())

sat = 0
for i in range(l, h+1):
  strI = str(i)

  if "0" in strI:
    continue

  if len(strI) != len(set(list(strI))):
    continue

  digits = list(map(int, strI))
  impossible = False
  for digit in digits:
    # print('digit', digit, i)
    if i % digit != 0:
      impossible = True
      break
  if impossible:
    continue

  sat += 1

print(sat)