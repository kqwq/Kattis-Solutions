n=int(input())
t = list(map(int, input().split()))
t.sort()

mm = 0
for i, days in enumerate(t):
  mm = max(mm, days-i+n+1)

print(mm)