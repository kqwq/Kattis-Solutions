input()
bats = map(int, input().split())
bats = list(filter(lambda x:x>=0, bats))
print(sum(bats)/len(bats))