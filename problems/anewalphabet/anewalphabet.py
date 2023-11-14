


newAlphabet = "@,8,(,|),3,#,6,[-],|,_|,|<,1,[]\\/[],[]\\[],0,|D,!!!,|Z,$,'][',|_|,\\/,\\/\\/,}{,`/,2".split(",")
newAlphabet[newAlphabet.index("!!!")] = "(,)"

# print(len(newAlphabet))
line = input()
newLine = ""
for char in line:
  n = ord(char.upper())-65
  if n >= 0 and n < 26:
    newLine += newAlphabet[n]
  else:
    newLine += char

print(newLine)