
counts = {}

for card in input().split():
  rank, suit = list(card)

  if rank in counts:
    counts[rank] += 1
  else:
    counts[rank] = 1

highest = max(counts.values())
print(highest)