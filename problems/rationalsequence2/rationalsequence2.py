'''
approach

let's find a way to traverse the tree upwards and store the directions we choose.



'''


n = int(input())

for i in range(n):
  k, pqBoth = input().split()
  p, q = map(int, pqBoth.split("/"))
  directions = []

  while p != q:
    if p > q:
      directions.append(0) # go up-left
      p -= q
    else:
      directions.append(1) # go up-right
      q -= p

  tot = 1
  for j, d in enumerate(directions[::-1]):
    tot *= 2
    if not d:
      tot += 1
  
  print(k, tot)
  
  



