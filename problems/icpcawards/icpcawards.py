n = int(input())

won = {}

printed = 0
for i in range(n):
  uni, team = input().split()

  if uni in won:
    continue

  print(uni, team)
  printed += 1
  if printed >= 12:
    break
  won[uni] =1