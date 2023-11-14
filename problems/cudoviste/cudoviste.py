r,c=map(int,input().split())

m = []
for i in range(r):
    m.append(list(input()))

smash = [0,0,0,0,0]
for i in range(r - 1):
    for j in range(c - 1):
        spaces = [m[i][j],m[i][j+1],m[i+1][j],m[i+1][j+1]]
        if "#" in spaces:
            continue
        smash[spaces.count("X")] += 1
for s in smash:
    print(s)