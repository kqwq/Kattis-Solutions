judges,n=map(int, input().split())
minSum=(judges-n)*-3
maxSum=(judges-n)*3
for i in range(n):
    r = int(input())
    minSum+=r
    maxSum+=r
print(minSum/judges,maxSum/judges)
    