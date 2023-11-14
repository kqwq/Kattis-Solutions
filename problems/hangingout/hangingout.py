'''
COMPILER ERROR - program doesn't even run in the first place

RUNTIME ERROR - program crashes while running

LOGIC ERROR - program runs fine, but wrong answer


'''

l, x = map(int, input().split())


curr = 0
denied = 0
for i in range(x):
  line = input()
  action, _num = line.split()
  num = int(_num)
  if action =="enter":
    if curr <= l - num:
      curr+=num
    else:
      denied += 1
  else:
    curr -= num
print(denied)
  
  


