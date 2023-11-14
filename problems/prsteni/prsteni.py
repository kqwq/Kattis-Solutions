import math
input()
x = list(map(int, input().split()))
first = x[0]
rest = x[1:]
for gear in rest:
  gcd = math.gcd(first, gear)
  print( first//gcd,"/",   gear//gcd,  sep="")
  