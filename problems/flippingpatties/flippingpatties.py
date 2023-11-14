n = int(input())


ocupied = [0] * (43200+10)
for i in range(n):
  di, ti = map(int, input().split())
  ocupied[ti] += 1
  ocupied[ti-di] += 1
  ocupied[ti-di*2] += 1

print((max(ocupied)+1) // 2)
