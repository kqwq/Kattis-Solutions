
n = int(input())
seq = []

for i in range(n):
  seq.append(input())

s = 0
for i, x in enumerate(seq[::-1]):
  if x == "O":
    s += 2 ** (0+ i)

print(s)