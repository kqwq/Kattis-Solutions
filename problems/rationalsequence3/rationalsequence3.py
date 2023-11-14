


cases = int(input())

for case in range(cases):
  _, n = map(int, input().split())

  binN = bin(n)[2:] # sequence of left and right turns in reverse order
  # 0=left, 1=right
  if binN == "0": binN = ""
  # print('bin', binN)

  p = 1
  q = 1
  for digit in binN[1:]:
    if digit == '0':
      q += p
    else:
      p += q
  
  print(case+1, str(p)+"/"+str(q))
