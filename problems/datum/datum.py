
d, m = map(int, input().split())

words = list(map(lambda x:x+"day", ["Mon", "Tues", "Wednes", "Thurs", "Fri", "Satur", "Sun"]))
months = [31,28,31,30,31,30,31,31,30,31,30,31]

onM = 1
while onM < m:
  d += months[onM-1]

  onM += 1

print(words[(d+2) % 7])