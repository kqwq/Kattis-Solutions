a,b=map(int,input().split())
if a>b:a,b=b,a
for i in range(a+1, b+2):
    print(i)