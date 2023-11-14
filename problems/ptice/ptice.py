
input()

seq = input()
a=0
b=0
g=0

for i, c in enumerate(seq):
  a += c == "ABC"[i % 3]
  b += c == "BABC"[i % 4]
  g += c == "CCAABB"[i % 6]

mostCorrect = max(a,b,g)
mostCorrectNames = []
if a == mostCorrect:
  mostCorrectNames.append("Adrian")
if b == mostCorrect:
  mostCorrectNames.append("Bruno")
if g == mostCorrect:
  mostCorrectNames.append("Goran")

print(mostCorrect)
for name in mostCorrectNames:
  print(name)