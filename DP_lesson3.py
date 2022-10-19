n = int(input())
a = []
for i in range(n):
  a.append(int(input()))

A = int(input())

dp =[[False for i in range(101)] for j in range(10001)]
dp [0][0] = True
for i in range(n):
  for j in range(A+1):
    dp[i + 1][j] |= dp[i][j] 
    if j >= a[i] :
      dp[i + 1][j] |= dp[i][j-a[i]] 

if dp[n][A]:
  print("yes")
else:
  print("no")