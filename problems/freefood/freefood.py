n = int(input())
events = []
for i in range(n):
  events.append(list(map(int, input().split())))

times = 0
for i in range(0, 366):
  for ev in events:
    if i >= ev[0] and i <= ev[1]:
      times += 1
      break

print(times)