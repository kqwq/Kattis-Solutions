n,dm = map(int, input().split())
d = list(map(int,input().split()))

for k, i in enumerate(d):
  if i <= dm:
    print("It hadn't snowed this early in {} years!".format(k))
    quit()
print("It had never snowed this early!")