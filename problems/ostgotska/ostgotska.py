


line = input()

words = line.split()

aeTimes = 0
for word in words:
  if "ae" in word:
    aeTimes += 1

freq = aeTimes / len(words)

if freq >= 0.4:
  print("dae ae ju traeligt va")
else:
  print("haer talar vi rikssvenska")