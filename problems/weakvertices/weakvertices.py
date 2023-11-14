
while 1:
  n = int(input())
  if n == -1:
    break
  graph = []
  for i in range(n):
    graph.append(list(map(int, input().split())))
  
  # find triangles
  weak = set()
  for i in range(n):
    gi = graph[i]
    friendsI = []
    for j, v in enumerate(gi):
      if v: friendsI.append(j)
    # friendsI is now constructed! It holds the indices of our neighbors
    for fi in friendsI:
      # fi is the friend index
      # let's see if any of fi's friends are also in fi
      for j in range(n):
        if graph[fi][j] and j in friendsI:
          weak.add(i)

  nonWeaks = []
  for i in range(n):
    if i not in weak:
      nonWeaks.append(str(i))
  print(" ".join(nonWeaks))
  

    