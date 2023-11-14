

while 1:
  w, l = map(int, input().split())
  thinks = [0, 0]
  acktualllllyyy = [0, 0]
  if w == 0 and l == 0:
    quit()
  n = int(input())
  for i in range(n):
    direction, amount_ = input().split()
    amount = int(amount_)
    if direction == "u":
      thinks[1] += amount
      acktualllllyyy[1] += amount

    elif direction == "d":
      thinks[1] -= amount
      acktualllllyyy[1] -= amount

    if direction == "l":
      thinks[0] -= amount
      acktualllllyyy[0] -= amount
    elif direction == "r":
      thinks[0] += amount
      acktualllllyyy[0] += amount

    acktualllllyyy[0] = max(0, min(w-1, acktualllllyyy[0]))
    acktualllllyyy[1] = max(0, min(l-1, acktualllllyyy[1]))

  print("Robot thinks", *thinks)
  print("Actually at", *acktualllllyyy)
  print()
