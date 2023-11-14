n=int(input())

for i in range(n):
    _, days = map(int, input().split())
    x = days + 1
    candles = x * (x + 1) / 2
    print(i+1, int(candles-1))