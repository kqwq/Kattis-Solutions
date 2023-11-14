
n = int(input())
stacks = list(map(int, input().split()))
stacksLeft = stacks[:]

# Quickly determine if it's possible
total = sum(stacks)
if total % 2 == 1:
  print("no")
  quit()



# 2 pointer solution
# p1 and p2 are the highest and 2nd highest values, not neccessarily in that order
pointers = []
steps = []

while total > 0:
  a = min(x for x in stacks if x)
  ai = stacks.index(a)
  b = max(x for x in stacks if x)
  bi = n - 1 - stacks[::-1].index(b)

  if ai == bi:
    print("no")
    quit()
  steps.append([ai+1, bi+1])
  stacks[ai] -= 1
  stacks[bi] -= 1
  if stacks[ai] == 0:
    stacks[ai] = None
  if stacks[bi] == 0:
    stacks[bi] = None
  total -= 2

print("yes")
for step in steps:
  print(step[0], step[1])
