d = int(input())
shares = 0
money = 100
p = []

for i in range(d):
  p.append(int(input()))
p.append(0)

for i in range(d):
  pNow = p[i]
  pNext = p[i+1]
  
  if pNext > pNow:
    # buy all shares
    canBuyShares = min(100_000-shares, money // pNow)
    shares += canBuyShares
    money -= pNow * canBuyShares

  elif pNext < pNow:
    # sell all shares
    canSellShares = shares
    shares = 0
    money += pNow * canSellShares

print(money + shares * p[-1])