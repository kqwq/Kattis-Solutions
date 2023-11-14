
r,_,zr,zc=map(int,input().split())
for i in range(r):
  line = input()
  cc = ""
  for char in line:
    cc += char * zc
  for j in range(zr):
    print(cc)
  