

p, d = map(int, input().split())

votes = [[0] * 2 for _ in range(d)]

for i in range(p):
  di, ai, bi = map(int, input().split())
  votes[di-1][0] += ai
  votes[di-1][1] += bi

allVotes = 0
aaa = 0
bbb = 0
for vote in votes:
  [ai, bi] = vote
  total = ai + bi
  overcome = total // 2 + 1
  aWins = ai > bi
  winner = "A" if aWins else "B"
  aWasted = 0
  bWasted = 0
  if aWins:
    aWasted = ai - overcome
    bWasted = bi
  else:
    aWasted = ai
    bWasted = bi - overcome
  aaa += aWasted
  bbb += bWasted
  allVotes += ai + bi
  print(winner, aWasted, bWasted)
print(abs(aaa-bbb)/allVotes)
