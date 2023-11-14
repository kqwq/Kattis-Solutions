line1 = input().split()
a,b = map(int,input().split())

kernels = 0
for i in range(5):
  kernels += int(line1[i*2])*int(line1[i*2+1])
kernels = int(kernels / 5)

tot = a*kernels / b
print(int(tot))