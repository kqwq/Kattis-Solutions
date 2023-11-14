


n = int(input())


hash = {}
for i in range(n):
  c = map(str,sorted(map(int, input().split())))
  cc=" ".join(c)

  if cc in hash:
    hash[cc] += 1
  else:
    hash[cc] = 1

m =max(hash.values())
mc = 0
for h in hash.values():
  if h == m:
    mc += m
print(mc)
