
n, prediction, s = map(int, input().split())

for i in range(s):
  ms = list(map(int, input().split()))[1:]
  if prediction in ms:
    print("KEEP")
  else:
    print("REMOVE")