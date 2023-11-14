

setN = 1
while 1:
  n = int(input())
  if n == 0:
    quit()
  
  print("SET", setN)
  setN += 1
  s = []
  for i in range(n):
    s.append(input())
  s.sort(key=lambda x:len(x))
  i = 0
  asc = True
  while len(s):
    if asc:
      print(s.pop(i))
      i += 1
      if i >= len(s):
        asc = False
    else:
      print(s.pop())


