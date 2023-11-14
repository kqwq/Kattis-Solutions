
def swap(li, b, c):
  li[b], li[c] = li[c], li[b] 

seq = list(map(int,input().split()))

while seq != sorted(seq):
  if seq[0] > seq[1]:
    swap(seq, 0, 1)
    print(*seq)
  if seq[1] > seq[2]:
    swap(seq, 1, 2)
    print(*seq)
  if seq[2] > seq[3]:
    swap(seq, 2, 3)
    print(*seq)
  if seq[3] > seq[4]:
    swap(seq, 3, 4)
    print(*seq)