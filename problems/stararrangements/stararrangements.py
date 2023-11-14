
s = int(input())

print("{}:".format(s))

for i in range(2, s//2 + 2):
  # print(i)
  #a,a-1
  iLess = i - 1
  if s % (i + iLess) == 0:
    print("{},{}".format(i, iLess))

  
  #(a,a-1)*repeat,a
  iLess = i - 1
  if s % (i + iLess) == i:
    print("{},{}".format(i, iLess))

  #a,a
  if s % i == 0:
    print("{},{}".format(i, i))
