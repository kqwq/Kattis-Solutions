
t = int(input())
for i in range(t):
  n = int(input())
  x = list(map(int, input().split()))
  low = min(x)
  high = max(x)
  res = (high - low) * 2
  print(res)