from functools import reduce

n = int(input())
while n > 9:
  n = reduce(lambda a,b:a*b,filter(lambda x:x,map(int,str(n))))


print(n)