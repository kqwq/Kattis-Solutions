x=int(input())
n=int(input())
has = x
for i in range(n):
    has += x - int(input())
print(has)
