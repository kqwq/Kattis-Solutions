

seq = []
line = input()
for char in line:
  a = "000"+bin(int(char))[2:]
  a = a.replace("0", ".").replace("1", "*")
  seq.append(a)


for i in range(4):
  pos = -4+i
  print(seq[0][pos], seq[1][pos], " ", seq[2][pos], seq[3][pos])
