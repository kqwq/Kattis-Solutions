input()

d = list(map(int, input().split()))

m = min(d)
for i in range(len(d)):
  if d[i] == m:
    print(i)
    quit()