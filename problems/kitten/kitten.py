stuck = input()

branches = []
while 1:
  inp = input()
  if inp == "-1":
    break
  branches.append(inp.split())

path = [stuck]
change = True
while change:
  # print(path)
  change = False
  for branch in branches:
    if stuck in branch[1:]:
      path.append(branch[0])
      stuck = branch[0]
      change = True
      break

print(*path)