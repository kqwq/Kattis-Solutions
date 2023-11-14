


b1, b2, b3, b4, b5, b6, h1, h2 = map(int, input().split())

r = [b1, b2, b3, b4, b5, b6]


for i in range(0, 4):
  for j in range(i+1, 5):
    for k in range(j+1, 6):
      if r[i] + r[j] + r[k] == h1:
        stack1 = [r[i], r[j], r[k]]
        stack2 = []
        otherI = []
        for l in range(0, 6):
          if l not in [i, j, k]:
            stack2.append(r[l])
        stack1.sort(reverse=True)
        stack2.sort(reverse=True)
        both = stack1 + stack2
        print(*both)
        quit()