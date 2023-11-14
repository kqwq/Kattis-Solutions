n=int(input())
for i in range(n):
    line=input().split()
    b=int(line[0])
    p=float(line[1])
    calc = 60 * b / p
    maxPass = 60 * (b+1) / p
    minPoss = 60 * (b-1) / p
    print(minPoss, calc, maxPass)