

def get_uniq(li):
  counts = {}
  for num in li:
    if num in counts:
      counts[num]+=1
    else:
      counts[num] = 1
  for key, val in counts.items():
    if val == 1:
      return key


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4 = get_uniq([x1, x2, x3])
y4 = get_uniq([y1, y2, y3])
print(x4, y4)