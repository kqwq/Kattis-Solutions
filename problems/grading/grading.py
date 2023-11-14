

a = "ABCDEF"

grades = list(map(int, input().split()))
g = int(input())

for i in range(5):
  if g >= grades[i]:
    print(a[i])
    quit()
print("F")