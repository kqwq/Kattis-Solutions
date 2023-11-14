




for i in range(int(input())):
  line = input()
  if "+" in line:
    print(sum(map(int, line.split("+"))))
  else:
    print("skipped")