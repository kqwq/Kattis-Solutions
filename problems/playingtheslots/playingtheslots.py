import math


# Helper function to calculate distance from line (m, b) and point (x, y)
def distFromLine(m, b, x, y):
  m2 = - 1 / (m + 0.0000000001)
  b2 = y - m2 * x 
  xOnLine = (b2 - b) / (m - m2)
  yOnLine = m * xOnLine + b 
  res = math.sqrt((xOnLine - x)**2 + (yOnLine - y)**2)
  return res

# Number of sides (first input)
sides = int(input())

# Create an array of points [ [x1, y1], [x2, y2], [x3, y3] ...]
points = []
for i in range(sides):
  x, y = map(float, input().split())
  points.append([x,y])

# Set minimum furthest to practically infinity
minFurthest = 99999

# For every edge...
for i in range(len(points)):
    
  # Let p1 and p2 be 2 adjacent points on the polygon
  p1 = points[i]
  p2 = points[(i + 1) % len(points)]

  # Find the line that intersects p1 and p2
  deltaX = p2[0] - p1[0]
  deltaY = p2[1] - p1[1]
  lineSlope = deltaY / (deltaX + 0.0000000001)
  yIntersect = p1[1] - lineSlope * p1[0]

  # Find the furthest point from that line
  furthest = 0
  for j in range(len(points)):
    pj = points[j]
    dist = distFromLine(lineSlope, yIntersect, pj[0], pj[1])
    furthest = max(furthest, dist)
    
  # Update minimum furthest
  minFurthest = min(minFurthest, furthest)
  
# Return minimum furthest
print(minFurthest)