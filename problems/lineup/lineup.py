n=int(input())

words = []

for i in range(n):
  words.append(input())

if words == sorted(words):
  print("INCREASING")
elif words == sorted(words, reverse=True):
  print("DECREASING")
else:
  print('NEITHER')