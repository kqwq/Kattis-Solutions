
import math


while 1:
  r,m,c = map(float, input().split())
  if r == 0:
    break
  print(r**2*math.pi, 4*r*r*c/m)