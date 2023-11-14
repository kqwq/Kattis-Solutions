

def isHarshad(n):
    digits = map(int, str(n))
    sumDigits = sum(digits)
    return n % sumDigits == 0


n = int(input())
while 1:
    if isHarshad(n):
        print(n)
        quit()
    n += 1
