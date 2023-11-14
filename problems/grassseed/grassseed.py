c=float(input())
n=int(input())
sum=0
for i in range(n):
    w,l=map(float,input().split())
    sum+=w*l*c
print(sum)