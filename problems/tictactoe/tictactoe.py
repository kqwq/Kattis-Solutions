
# Input
n, m = map(int, input().split())

# If n=1, special case.
if n == 1:
  miniBoard = input()
  if miniBoard == ".":
    print("IN PROGRESS")
  elif miniBoard == "X":
    print("X WINS")
  else:
    print("ERROR")
  quit()


theBoard = ""
numXs = 0
numOs = 0
for i in range(n):
  line = input()
  numXs += line.count("X")
  numOs += line.count("O")
  theBoard += line
  
# Helper functions
def every(board, rang, match):
  for i in rang:
    # if i < 0 or i >= len(board):
    #   continue
    if board[i] != match:
      return False
  return True

def incrementHash(hash, key):
  if key in hash:
    hash[key] += 1
  else:
    hash[key] = 1

def xWins(numXs, numOs):
  if numXs == numOs:
    print("ERROR")
  else:
    print("X WINS")
  quit()

def oWins(numXs, numOs):
  if numXs == numOs:
    print("O WINS")
  else:
    print("ERROR")
  quit()

# VarS
numXSolutions = 0
numOSolutions = 0
solutionsHash = {} # Hash of cells that are part of a solution.
# ex: { "4_5": 1, "4_6": 3, "4_7": 1 }
# The 3 value means the 4_6 cell is part of 3 separate solutions.
# A board is not valid if more than 2 values in this solutionsHash
#  are more >1. The board is also not valid if more than 2 solutions
#  exist and no overlaps exist (==1 for every value in solutionsHash)

# Check if game state is impossible based on # of Xs and Os
if numXs > numOs + 1 or numXs < numOs:
  print("ERROR")
  quit()

# Build array of bs (board sections)
bs = [] # ex: [ [4, 14, 24], [5, 15, 25], ... ]

# Check horizontal
for y1 in range(n):
  for x1 in range(0, n-m+1):
    y2 = y1
    x2 = x1 + m
    incr = 1
    r = range(x1+y1*n, x2+y2*n, incr)
    bs.append(r)


# Check vertical
for x1 in range(n):
  for y1 in range(0, n-m+1):
    y2 = y1 + m
    x2 = x1
    incr = n
    r = range(x1+y1*n, x2+y2*n, incr)
    bs.append(r)

# Diagonal 1
for x1 in range(n - m + 1):
  for y1 in range(n - m + 1):
    y2 = y1 + m
    x2 = x1 + m
    incr = n + 1
    r = range(x1+y1*n, x2+y2*n, incr)
    bs.append(r)

# Diagonal 2
for bboxX1 in range(n - m + 1):
  for y1 in range(n - m + 1):
    x1 = bboxX1 + m - 1
    x2 = bboxX1 - 1
    y2 = y1 + m
    incr = n - 1
    r = range(x1+y1*n, x2+y2*n, incr)
    bs.append(r)

# Check every board section
solutionsRanges = []
for range_obj in bs:
  # print(range_obj)
  if every(theBoard, range_obj, "X"):
    numXSolutions += 1
    solutionsRanges.append(range_obj)
    for i in range_obj:
      incrementHash(solutionsHash, i)

  if every(theBoard, range_obj,  "O"):
    numOSolutions += 1
    solutionsRanges.append(range_obj)
    for i in range_obj:
      incrementHash(solutionsHash, i)

# If both sides win
if numXSolutions and numOSolutions:
  print("ERROR")
  quit()

# If there's simply 1 X solution
elif numXSolutions == 1:
  xWins(numXs, numOs)

# If there's simply 2 O solutions
elif numOSolutions == 1:
  oWins(numXs, numOs)

# If nobody won
if numXSolutions == 0 and numOSolutions == 0:
  if numXs + numOs == n ** 2:
    print("DRAW")
  else:
    print("IN PROGRESS")
  quit()

# If X (or O) has multiple solutions...

# Now we need to see if a single point contains all the solutions
# Find max value and its position
maxVal = 0
intersectionPosTest = None # Intersection point to test
for position, value in solutionsHash.items():
  if value > maxVal:
    maxVal = value
    intersectionPosTest = position
# print(solutionsRanges, intersectionPosTest)


# Check every board again
for range_obj in solutionsRanges:
  intersectionFound = False
  for i in range_obj:
    if i == intersectionPosTest:
      intersectionFound = True
  if not intersectionFound:
    print("ERROR")
    quit()

if numXSolutions > 0:
  xWins(numXs, numOs)
else:
  oWins(numXs, numOs)