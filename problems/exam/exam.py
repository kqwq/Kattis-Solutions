friend_correct=int(input())
m=list(input())
f=list(input())
n=len(m)
same=0
for i in range(n):
    if m[i] == f[i]:
        same += 1
diff = n - same

# Calculate max # you got right
x = friend_correct + diff
if x > n:
    x = n - x
if x < 0:
    x += n
print(x)