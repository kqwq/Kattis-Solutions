
# Get our inputs
n = int(input())
lines = []
for i in range(n):
  lines.append(input())

# Here we are building 3 very important arrays
currLevel = 0
levels = [] # levels[i] is the number of layers deep for the i-th line
s = [] # s[i] is the number of spaces for the i-th line
t = [] # t[i] is the number of tabs for the i-th line
for line in lines:
  if line.endswith("{"):
    currLevel += 1
  elif line.endswith("}"):
    currLevel -= 1
  levels.append(currLevel - line.endswith("{")) 
  s.append(line.count('s'))
  t.append(line.count('t'))

# Ok, now that we got the data we needed, let's find the replacement factor x
for x in range(1, 1001):
  # OK HERE'S THE DEAL
  # For every i... this must hold true:
  # levels[i] * k = s[i] + t[i] * x
  # where k is some constant we have to compute.

  # First, let's find k
  valid = True
  previousK = None
  for i in range(n):
    leftSide = levels[i]
    rightSide = s[i] + t[i] * x
    if rightSide > 0 and leftSide > 0:
      currentK = rightSide / leftSide # This computes k
      if previousK != None:
        if previousK != currentK:
          valid = False
          break
      previousK = currentK
      
  if not valid:
    continue

  # Ok now that we calculated k, let's check if it works for all values
  k = previousK
  if k == None:
    k = 0
  for i in range(n):
    leftSide = levels[i]
    rightSide = s[i] + t[i] * x  
    if leftSide * k != rightSide:
      valid = False
      break
  
  if valid:
    print(x) # We found an x, k such that levels[i]*k=s[i]+t[i]*x
    quit()
print(-1)