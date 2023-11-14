
p = int(input())

for i in range(p):
    k, n = map(int, input().split())
    s1 = (n ** 2 + n) // 2
    s2 = n ** 2
    s3 = n ** 2 + n
    print(k, s1, s2, s3)
