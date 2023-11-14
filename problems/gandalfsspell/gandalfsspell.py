




chars = input()
words = input().split()

if len(chars) != len(words): 
  print("False")
  quit()

m = {}
m2 = {}

for i in range(0, len(words)):
  c = chars[i]
  w = words[i]
  # print(i, c, w,m)
  if c in m:
    if m[c] != w:
      print("False")
      quit()

  if w in m2:
    if m2[w] != c:
      print("False")
      quit()
  
  else:
    m[c] = w
    m2[w] = c

print("True")
