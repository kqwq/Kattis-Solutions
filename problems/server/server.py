n,t=map(int,input().split())
m=list(map(int,input().split()))
m.append(float("inf"))
ss = 0
for i, val in enumerate(m):
  ss += val
  if ss > t:
    print(i)
    quit()