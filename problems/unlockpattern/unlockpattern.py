
import math

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
nums = [] # [order(start=0), x, y]
for y, line in enumerate([line1, line2, line3]):
  for x, num in enumerate(line):
    nums.append([num-1, x, y])

totalDist = 0
nums.sort(key=lambda x:x[0]) # sort by order
for i in range(len(nums)-1):
  a = nums[i]
  b = nums[i+1]

  dist = math.dist(a[1:], b[1:])
  totalDist += dist


print(totalDist)