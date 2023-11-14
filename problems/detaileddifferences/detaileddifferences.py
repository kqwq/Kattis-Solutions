n = int(input())

for i in range(n):
    a = input()
    b = input()
    diff = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            diff += "."
        else:
            diff += "*"
    print(a)
    print(b)
    print(diff)
    print()