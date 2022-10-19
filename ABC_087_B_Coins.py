a, b, c, x = map(int, input().split())

res = 0
for i in range(0, a):
  for j in range(0, b):
    for k in range(0, c):
      if x == (500*i + 100*j + 50*k):
        res = res+1

print(res)


