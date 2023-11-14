
n = int(input())

a = input()
b = input()

for i in range(len(a)):
  if (n % 2 == 0) != (a[i] == b[i]):
    print("Deletion failed")
    quit()
print("Deletion succeeded")
