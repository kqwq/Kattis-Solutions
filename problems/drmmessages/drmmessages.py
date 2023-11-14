def valOf(x):
  return ord(x) - 65
def rotate(x, byAmount):
  return chr(65 + ((valOf(x) + byAmount) % 26))

drm = input()

mid = len(drm) // 2
m1 = drm[:mid]
m2 = drm[mid:]

rotValue = sum(map(valOf, m1))
rotValue2 = sum(map(valOf, m2))
newValue = ""
newValue2 = ""
for c in m1:
  newValue += rotate(c, rotValue)
for c in m2:
  newValue2 += rotate(c, rotValue2) 

# print(newValue,newValue2)
# merge
finalValue = ""
i=0
for c in newValue:
  finalValue += rotate(newValue2[i], valOf(c))
  i += 1

print(finalValue)