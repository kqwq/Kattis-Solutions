

import sys

for line in sys.stdin:

  zeros = 0
  ones = 0

  for char in line:
    binCode = bin(ord(char))[2:]
    if binCode == "1010": # binCode of EOF
      continue
    binCode = "0" * (7 - len(binCode)) + binCode
    zeros += binCode.count("0")
    ones += binCode.count("1")

  if ones % 2 == 0 and zeros % 2 == 0:
    print("free")
  else:
    print("trapped")
