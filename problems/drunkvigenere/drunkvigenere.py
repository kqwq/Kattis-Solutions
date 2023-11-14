msg = input()
key = input()

ori = ""

for i, char in enumerate(msg):
  shift = ord(key[i]) - 65

  pos = ord(char) - 65
  if i % 2 == 0:
    pos -= shift
  else:
    pos += shift
  
  if pos < 0:
    pos += 26
  elif pos >= 26:
    pos -= 26
  
  ori += chr(pos + 65)

print(ori)