input()
s = input()
i=1
c=0
while c<len(s):
    iStr = str(i)
    iLen = len(iStr)
    if s[c:c+iLen]!=iStr:
        print(i)
        quit()
    c+=iLen
    i+=1
print(i)