m=int(input())
n=int(input())

empty=0
for i in range(n):
  empty+=input().count(".")

print(empty/m/n)