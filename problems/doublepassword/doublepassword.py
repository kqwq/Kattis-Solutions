a=input()
b=input()
diff=0
for i in range(4):
  if a[i]!=b[i]:
    diff+=1

print(2**diff)