n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(sum(set(x).difference(y)))