

a = list(input())
b = list(input())
while len(a) < len(b):
  a.insert(0,"0")
while len(b) < len(a):
  b.insert(0,"0")

for i in range(len(a)):
  if int(a[i]) > int(b[i  ]):
    b[i] = ""
  elif int(a[i]) < int(b[i]):
    a[i] = ""

a = "".join(a)
b = "".join(b)
line1 = int(a) if len(a) else "YODA"
line2 =  int(b) if len(b) else "YODA"
print(line1)
print(line2)