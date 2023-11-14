orders = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]
n = int(input())


nsb = []
for i in range(n):
  nsb.append(int(input()))


bestBestScore = 0
for order in orders:
  ZERO = order[0]
  ONE = order[1]
  TWO = order[2]
  a = n 
  b = n
  mids = [0, 0, 0]
  # left of a is 0s
  # between a and b is 1s
  # right of b is 2s
  zerosInA = nsb.count(ZERO)
  onesInB = 0
  twosInC = 0
  bestScore = zerosInA + onesInB + twosInC
  while a > 0:
    # For every iteration of the a pointer moving over, 
    # find the best possible place for b to be, maximizing score

    # If the more front item is 0, decrement a
    a -= 1
    curr = nsb[a]
    if curr == ZERO:
      zerosInA -= 1
    elif curr == ONE:
      onesInB += 1

    # Increment the mids[curr]
    mids[curr] += 1

    # Decide whether to move over b to maximize score
    # To do this, we see if mids[2] > mids[1].
    # If so, move over b and update affected variables
    if mids[TWO] > mids[ONE]:
      b = a
      onesInB = 0
      twosInC += mids[TWO]
      mids = [0, 0, 0]
    
    # Calculate score
    score = zerosInA + onesInB + twosInC
    # print("-{}-{}- : {} from {}+{}+{}".format(a,b,score,zerosInA,onesInB,twosInC))
    bestScore = max(bestScore, score)
  bestBestScore = max(bestBestScore, bestScore)
print(bestBestScore)