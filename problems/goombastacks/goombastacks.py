n=int(input())
tot=0
for i in range(n):
    g,b=map(int,input().split())
    tot+=g
    if tot < b:
        print("impossible")
        quit()
    
    
print("possible")