



n = int(input())
printers = 1
times = 0
while n > 0:
  if printers < n:
    printers *= 2
  else:
    n = 0
  times += 1
print(times)