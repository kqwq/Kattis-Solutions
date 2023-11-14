classrooms, inv = map(int,input().split())
needs = 0
for i in range(classrooms):
    needs += int(input())
if inv >= needs:
    print("Jebb")
else:
    print("Neibb")