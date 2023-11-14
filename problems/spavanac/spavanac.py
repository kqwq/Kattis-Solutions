



h,m = map(int,input().split())
mm = h * 60 + m

mm -= 45
if mm < 0:
  mm += 24 * 60

print(mm // 60, mm % 60)