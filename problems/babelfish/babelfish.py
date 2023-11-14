import sys

dMode = True
d = {}
for line in sys.stdin:
  line = line.strip()
  if dMode:
    parts = line.split()
    if len(parts) == 0:
      dMode = False
      continue

    english, babelfish = parts
    d[babelfish] = english

  else:
    if line in d:
      print(d[line])
    else:
      print("eh")