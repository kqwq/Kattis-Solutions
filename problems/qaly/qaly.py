n=int(input())
sum=0
for i in range(n):
    a,b=map(float,input().split())
    sum+=a*b
print(sum)