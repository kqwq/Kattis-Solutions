n,m=map(int,input().split())

costs = {
  ".": 20,
  "O": 10,
  "\\": 25,
  "/": 25,
  "A": 35,
  "^": 5,
  "v": 22
}
co = 0
for i in range(n):
  for c in input():
    co+=costs[c]

print(co)