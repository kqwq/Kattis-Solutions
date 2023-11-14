a,b=map(int,input().split())

if a+b ==0:
  print("Not a moose")
  quit()
s = a + b
m = max(a, b) * 2
if a == b:
  print("Even", m)
else:
  print("Odd", m)