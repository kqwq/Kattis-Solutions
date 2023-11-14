r,n=map(int,input().split())
rooms=[]

for i in range(n):
  rooms.append(int(input()))

for i in range(1,r+1):
  if i not in rooms:
    print(i)
    quit()
print('too late')