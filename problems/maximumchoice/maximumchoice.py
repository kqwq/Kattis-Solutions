
'''

n=100

b=1, mgap=50 (1,50),(50,100) which are 49,50
b=2, mgap=33 (1,34),(34,67),(67,100) which are 33,33,33
b=3, mgap=25 (1,26),(26,51),(51,77),(77,100) which are 25,25,25,23




'''


import math
n, b = map(int, input().split())



times = 0
while n > 0:
  nBetween = n - b
  largestGap = math.ceil(nBetween / (b + 1))
  n = largestGap
  times += 1
print(times)

