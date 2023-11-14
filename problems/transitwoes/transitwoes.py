import math
s, t, n = map(int, input().split())
# s is current time for our program

walk = list(map(int, input().split()))

bus = list(map(int, input().split()))
c = list(map(int, input().split()))



for i in range(n):
  s += walk[i]
  # wait for bus
  s = math.ceil(s / c[i]) * c[i]
  # take bus
  s += bus[i]



s += walk[-1]


if s <= t:
  print("yes")
else:
  print("no")