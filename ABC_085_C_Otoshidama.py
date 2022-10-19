N = int(input())
Y = int(input())


res10000 = -1
res5000 = -1
res1000 = -1
for a in range(N+1):
  for b in range(N+1 - a):
    c = N - a - b
    if Y == 10000*a + 5000*b + 1000*c:
      res10000 = a
      res5000 = b
      res1000 = c

print(res10000, res5000, res1000)
        

