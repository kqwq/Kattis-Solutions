

word = input()
letters = set(word)
seq = input()

correct = 0
i =0
while i < 10 + correct:
  guess = seq[i % len(seq)]
  if guess in letters:
    correct += 1
    letters.remove(guess)
  i += 1

if len(letters) == 0:
  print("WIN")
else:
  print('LOSE')