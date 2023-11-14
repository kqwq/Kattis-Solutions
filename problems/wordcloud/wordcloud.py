import math

caseN = 1
while 1:
  # Input
  w, n = map(int, input().split())
  if w == 0:
    break
  words = []
  cMax = 0
  for i in range(n):
    s, c_ = input().split()
    c = int(c_)
    cMax = max(c, cMax)
    words.append([s, c])

  # Vars
  cloudH = 0

  # Algorithm
  rowW = 0
  rowH = 0
  rowI = 0
  for word in words:
    s = word[0]
    c = word[1]
    t = len(s)
    P = 8 + math.ceil(40*(c-4)/(cMax-4))
    wordW = math.ceil(9 / 16 * t * P)
    
    # If first word...
    if rowH == 0 and rowW == 0:
      rowW += wordW
      rowH = max(rowH, P)

    # If space for another word
    elif rowW + 10 + wordW <= w:
      rowW += 10 + wordW
      rowH = max(rowH, P)

    # Else, create new row
    else:
      cloudH += rowH
      rowW = wordW
      rowH = P
      rowI += 1
      # print("at word", s, "created new row at ", rowI)

  # At the end, add  the final height
  cloudH += rowH


  # Output
  print("CLOUD " + str(caseN) + ":", cloudH)
  caseN += 1