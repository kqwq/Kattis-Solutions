

spellingBee = input()
center = spellingBee[0]
outer = spellingBee[1:]

correctWords = []

n = int(input())
for i in range(n):
  word = input()

  #2
  if len(word) < 4:
    continue

  #1
  bad = False
  for letter in word:
    if letter not in spellingBee:
      bad = True
      break
  if bad:
    continue

  #3
  if center not in word:
    continue

  print(word)
