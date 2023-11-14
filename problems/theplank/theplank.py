

'''
1 - 1
2 - 2
3 - 4
4 - 7 (ways to make 3 + ways to make 2 + ways to make 1)

'''

ways = [None,1,2,4,7]

n = int(input())

while n >= len(ways):
  i = len(ways) - 1
  su = ways[i] + ways[i-1] + ways[i-2]
  ways.append(su)
print(ways[n])