n = int(input())

popcorns = 0
# phase 1
popcorns += 2 * (n // 4 ) * (n // 4 - 1) 

# phase 2
popcorns += 4

print(popcorns)