n = int(input())
connections = set()
for i in range(n):
  line = input().split()
  for link in line[1:]:
    a = line[0]
    b = link
    if a > b: b, a = a, b
    connections.add((a, b))
start, dest = input().split()
connections = list(connections)


def findPath(currentPath, chooseFrom, destination):
  curr = currentPath[-1]
  # Choose all that have curr[-1]
  for branch in chooseFrom:
    a, b = branch
    if curr == b:
      a, b = b, a
    if curr == a:
      if destination == b:
        return currentPath + [b]
      cfcpy = chooseFrom[:]
      cfcpy.remove(branch)
      result = findPath(currentPath + [b], cfcpy, destination)
      if len(result) != 0:
        return result
  return []
  

res = findPath([start], connections, dest)
if len(res) == 0:
  print("no route found")
else:
  print(' '.join(res))
