

n = int(input())

for i in range(n):
  cmd = input()
  if "Simon says" in cmd:
    cmd = cmd.replace("Simon says ", "")
    print(cmd)