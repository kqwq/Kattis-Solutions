
def same(l, a, b, c):
  key = {
  "O": "Jebb",
  "X": "Neibb"
  }
  if l[a] != "_" and l[a] == l[b] and l[a] == l[c]:
    print(key[line[a]])
    quit()


line = ""

line += input()
line += input()
line += input()


for i in range(0, 3):
  same(line, i*3, i*3+1, i*3+2)
for i in range(0, 3):
  same(line, i, i+3, i+6)
same(line, 0, 4, 8)
same(line, 2, 4, 6)
print("Neibb")