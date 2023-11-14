
# rate of fuel = fuel consumed / time taken
# efficiency = velocity / rate of fuel
n = int(input())
d = float(input())

bestI = ""
bestE = -1
for i in range(n):
  initials, _v, _r = input().split()
  v = float(_v) # velocity of ship
  r = float(_r) # fuel consumed 

  timeTaken = d / v

  rateOfFuel = r / timeTaken
  efficiency = v / rateOfFuel
  if efficiency > bestE:
    bestE = efficiency
    bestI = initials

print(bestI)




