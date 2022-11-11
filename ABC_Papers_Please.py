N = int(input())
a = list(map(int, input().split()))

ret = True
for i in range(N):
  if (a[i] % 2 == 0):
    if(a[i] % 3 == 0) or(a[i] % 5 == 0):
      ret = True
    else:
      ret = False
      break

if ret == True:
  print("APPROVED")
else:
  print("DENIED")