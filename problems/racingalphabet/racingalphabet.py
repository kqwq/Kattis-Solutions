import math
radius = 60 / 2 # feet

def posOf(letter):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
  return alphabet.index(letter)

n = int(input())
for i in range(n):
  line = input()
  currPos = posOf(line[0])
  totalDist = 0
  for letter in line[1:]:
    letterPos = posOf(letter)
    # print(currPos, letterPos)
    if currPos < letterPos - 14:
      currPos += 28
    elif currPos > letterPos + 14:
      currPos -= 28
    diff = abs(currPos- letterPos)
    arcDistance = 2 * math.pi * radius * diff / 28
    totalDist += arcDistance 
    currPos = letterPos
  print(totalDist / 15 + len(line))

  