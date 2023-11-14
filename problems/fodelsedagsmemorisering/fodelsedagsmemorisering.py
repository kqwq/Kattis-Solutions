
n = int(input())


bdayHash = {}
for i in range(n):
  name, _like, birthday = input().split()
  like = int(_like)
  
  if birthday in bdayHash:
    if like > bdayHash[birthday][1]:
      bdayHash[birthday] = [name, like]
  else:
    bdayHash[birthday] = [name, like]

names = sorted(map(lambda a:a[0], bdayHash.values()))
print(len(names))
for n in names:
  print(n)
