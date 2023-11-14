s = set(list(input()))
m = input()
output = []
for word in m.split():
  found = False
  for char in word:
    if char in s:
      found = True
      break
  if found:
    output.append("*" * len(word))
  else:
    output.append(word)

print(*output)
      
  