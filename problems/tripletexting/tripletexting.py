

t = input()
l = len(t) // 3

a = t[0:l]
b = t[l:l*2]
c = t[l*2:]

o = ""
for i in range(l):
  options = [a[i], b[i], c[i]]
  options.sort()

  o += options[1]

print(o)