
x = int(input())
y=sorted(list(str(x)))


while x < 1_000_000:
  x += 1
  if sorted(list(str(x))) == y:
    print(x)
    quit()
    
print(0)