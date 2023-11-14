
n = int(input())

won = 0
for i in range(n):
  line = input()
  if "CD" not in line:
    won += 1
print(won)