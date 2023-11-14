

n, t = map(int, input().split())

durations = []
for i in range(n):
  durations.append(int(input()))

durations.sort()

for (i, d) in enumerate(durations):
  if d <= (i) * t:
    print("NO")
    quit()
print("YES")