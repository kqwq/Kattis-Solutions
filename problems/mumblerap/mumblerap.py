import re

input()
line = input()

match = re.findall(r'\d+', line)

nums = map(int, match)
print(max(nums))
