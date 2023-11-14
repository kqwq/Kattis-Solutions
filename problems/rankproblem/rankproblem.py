

teams, nGames = map(int, input().split())

rankings = []
for i in range(teams):
  rankings.append("T" + str(i + 1))

his = []
for i in range(nGames):
  result = input().split()
  his.append(result)

for game in his:
  a = game[0]
  b = game[1]
  ai = rankings.index(a)
  bi = rankings.index(b)
  if ai < bi:
    continue # Rankings don't change if better team wins
  else:
    # Remove the beaten team, then insert it in its new place
    rankings.remove(b)
    rankings.insert(ai, b)

print(" ".join(rankings))