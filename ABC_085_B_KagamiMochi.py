N = int(input())
d = list(map(int, input().split()))

num = [0] * (100)

for i in range(N):
  num[d[i]] += 1

ans = 0
for i in range(100):
  if num[i] > 0:
    ans += 1

print(ans)