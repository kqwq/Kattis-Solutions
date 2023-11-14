
def yearFromDate(date):
  return int(date.split("/")[0])

n = int(input())
for i in range(n):
  name, uDay, bDay, courses = input().split()

  isEli = None

  if yearFromDate(uDay) >= 2010:
    isEli = True
  elif yearFromDate(bDay) >= 1991:
    isEli = True
  elif int(courses) > 40:
    isEli = False




  if isEli == True:
    print(name, "eligible")

  if isEli == False:
    print(name, "ineligible")

  if isEli == None:
    print(name, "coach petitions")
