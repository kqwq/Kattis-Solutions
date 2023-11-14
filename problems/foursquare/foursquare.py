
import math
import sys
sys.setrecursionlimit(100)

# Inputs
w1, h1 = map(int, input().split())
w2, h2 = map(int, input().split())
w3, h3 = map(int, input().split())
w4, h4 = map(int, input().split())

# Get blocks and area
blocks = [(w1, h1), (w2, h2), (w3, h3), (w4, h4)]
area = w1 * h1 + w2 * h2 + w3 * h3 + w4 * h4
side = math.sqrt(area)
if side % 1 > 0: # If decimal edge, it's impossible to solve
  print(0)
  quit()
side = round(side)

def rotate(block):
  return (block[1], block[0])

def cavity(w, h, blocks):
  # print('cavity', w, h, blocks)
  if w < 0 or h < 0:
    return 0
  if w == 0 or h == 0:
    return 1
  
  # We can lay either 1 or 2 blocks to fill in a gap, leaving a rectangular cavity
  # Case 1: lay 1 block along either the left or bottom border
  for block in blocks:
    blockRest = blocks[:]
    blockRest.remove(block)

    # If side matches width... lay down flat
    if block[1] == w:
      block = rotate(block)
    if block[0] == w:
      # print('alpha')
      res = cavity(w, h-block[1], blockRest)
      if res: return res
      
    # If side matches height... push to right side
    if block[0] == h:
      block = rotate(block)
    if block[1] == h:
      # print('beta')   
      res = cavity(w-block[0], h, blockRest)
      if res: return res

  # Case 2: lay 2 blocks along only the bottom border
  # If can lay down 2 along width... lay both down flat (we don't also need to check for RIGHT SIDE for _reasons_)
  if len(blocks) == 4:
    combos = [ [blocks[0], blocks[1]], [blocks[0], blocks[2]], [blocks[0], blocks[3]], [blocks[1], blocks[2]], [blocks[1], blocks[3]], [blocks[2], blocks[3]]]
  elif len(blocks) == 3:
    combos = [  [blocks[0], blocks[1]], [blocks[0], blocks[2]], [blocks[1], blocks[2]] ]
  elif len(blocks) == 2:
    combos = [  [blocks[0], blocks[1]] ]
  else:
    combos = []
  for combo in combos:
    a, b = combo
    if a[0] == b[1]: # if one is sideways
      a = rotate(a)
    if a[0] < a[1]:
      a = rotate(a)
      b = rotate(b)
    if a[1] == b[1] and a[0] + b[0] == w:
      blockRest = blocks[:]
      try:
        blockRest.remove(a)
      except Exception:
        pass
      try:
        blockRest.remove(b)
      except Exception:
        pass
      # print('gamma')
      res = cavity(w, h - a[1], blockRest)
      if res: return res

  return 0


possible = cavity(side, side, blocks)
print(possible)

