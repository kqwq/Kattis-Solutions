n = int(input())
length = 0
for i in range(n):
    length += int(input())
length -= n
length += 1
print(length)