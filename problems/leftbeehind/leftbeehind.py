

while 1:

  a, b = map(int, input().split())
  if not a and not b:
    break

  if a + b == 13:
    print("Never speak again.")
  elif b > a:
    print("Left beehind.")
  elif a > b:
    print("To the convention.")
  else:
    print("Undecided.")