input()  # trash first input
inp = list(map(int, input().split()))

# we need to count the # of times that n[i] increases
count = 0
for i in range(len(inp)-1):
    if inp[i] < inp[i+1]:
        count += 1
print(count+1)
