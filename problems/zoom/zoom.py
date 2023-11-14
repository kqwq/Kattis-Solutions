


n, k = map(int, input().split())

nums = input().split()

nn = []
for i in range(k-1, n, k):
  nn.append(nums[i])

print(" ".join(nn))