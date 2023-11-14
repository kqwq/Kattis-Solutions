

seen = set()

for i in range(10):
    seen.add(int(input()) % 42)

print(len(seen))