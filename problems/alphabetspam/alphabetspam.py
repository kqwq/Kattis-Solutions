



white =0
lower=0
upper=0
symbol=0

s=input()
for c in s:
  if c == "_":
    white += 1
  elif ord(c) >= 65 and ord(c) < 65 + 26:
    upper += 1
  elif ord(c) >= 97 and ord(c) < 97 + 26:
    lower += 1
  else:
    symbol += 1

l = len(s)
print(white/l)
print(lower/l)
print(upper/l)
print(symbol/l)