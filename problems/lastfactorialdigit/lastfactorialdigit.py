n=int(input())
for i in range(n):
    x = int(input())
    product = 1
    for j in range(2, x+1):
        product *= j
    print(str(product)[-1])