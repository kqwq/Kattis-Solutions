

p = "PER"
s = input()
diff = 0

for i in range(len(s)):
  if s[i] != p[i % 3]: diff += 1
print(diff)