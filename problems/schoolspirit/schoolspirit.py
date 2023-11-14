

n = int(input())
s = []
for i in range(n):
  s.append(int(input()))

scoreNow = 0
for i, ss in enumerate(s):
  scoreNow += ss * (4/5) ** i
scoreNow /= 5

sl = []
for i in range(n):
  scoreLater = 0
  sCopy = s[:]
  sCopy.pop(i)
  for j, ss in enumerate(sCopy):
    scoreLater += ss * (4/5) ** j
  sl.append(scoreLater / 5)

print(scoreNow)
print(sum(sl) / len(sl))