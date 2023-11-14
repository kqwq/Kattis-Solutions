
line = input()


suits = ['P', 'K', 'H', 'T']

# Detect if there are 2 of the same cards
cards = set()
for i in range(0, len(line), 3):
  cards.add(line[i:i+3])

if len(cards) != len(line) // 3:
  print("GRESKA")
  quit()

out = []
for suit in suits:
  count = 13 - line.count(suit)
  out.append(str(count))

print(" ".join(out))

