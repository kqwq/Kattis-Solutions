

n = int(input())

inside = set()

for i in range(n):
  t, name = map(str, input().split())

  if t == "entry":
    if name not in inside:
      print(name, "entered")
      inside.add(name)
    else:
      print(name, "entered (ANOMALY)")
  else:
    if name in inside:
      print(name, "exited")
      inside.remove(name)
    else:
      print(name, "exited (ANOMALY)")


