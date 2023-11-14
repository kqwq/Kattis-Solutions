g,t,n=map(int, input().split())
sum_items=sum(map(int, input().split()))
print(int((g-t)*0.9-sum_items))