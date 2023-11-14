

cpus = mems = drives = 0
n = int(input())
for i in range(n):
  a, b, c = input().split()
  if a == "J":
    cpus += 1
  if b == "J":
    mems += 1
  if c == "J":
    drives += 1

print(min(cpus, mems, drives))