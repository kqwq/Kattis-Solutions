b = int(input())

d = input().split()

word = input()

digits = []
pos = 0 # pos
while pos < len(word):
  for i, dd in enumerate(d):
    if word[pos:pos+len(dd)] == dd:
      pos += len(dd)
      digits.append(i)
      break

val = 0
n = len(digits)
for i, digit in enumerate(digits):
  val += (b ** (n-i-1)) * digit

print(val)