
n = int(input())
hotels = list(map(int, input().split()))

poss = 36

ways = [None,None,1,2,3,4,5,6,5,4,3,2,1,None]

for hot in hotels:
  poss -= ways[hot]
print(1-poss/36)