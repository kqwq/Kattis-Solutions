input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
m = []

for i in range(len(a)):
  li = [a[i], b[i], c[i]]
  min_ = min(li)
  li.remove(min_)
  m.append(min(li))
  
print(*m)