import math

n=int(input())
for i in range(n):
  x,y= map(int, input().split())



  a=12
  b=-4*x-4*y
  c=x*y
  h = (-b - math.sqrt(b**2 - 4 * a * c)) / 2 /a
  print(h*(x-2*h)*(y-2*h))