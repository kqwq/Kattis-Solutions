k = int(input())
n = int(input())

exploded = None
onPlayer = k # 1-player 1, 8-player 8
timeLeft = 60 * 3 + 30
for i in range(n):
  t_, z = input().split()
  t = int(t_)

  timeLeft -= t
  if timeLeft <= 0:
    exploded = onPlayer
    timeLeft = float("inf")

  if z == "T":
    onPlayer += 1
    if onPlayer >= 9:
      onPlayer = 1
    continue
  if z == "N":
    continue
  if z == "P":
    continue

print(exploded)