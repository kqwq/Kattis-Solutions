n = int(input())
m = int(input())

roomSizeMin = m // n
roomSizeMax = roomSizeMin + 1
leftoverSize = m % n

for i in range(n):
    output = "*" * roomSizeMin
    if i < leftoverSize:
        output += "*"
    print(output)
    