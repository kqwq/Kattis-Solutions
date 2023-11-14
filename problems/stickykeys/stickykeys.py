


s = input()
ss = ""

lastC = ""
for c in s:
  if c != lastC:
    ss += c
  lastC = c

print(ss)