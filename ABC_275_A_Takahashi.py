N = int(input())
a = list(map(int, input().split()))

ret = 0
chk = 0
if N >= len(a):
  for i in range(N):
    if chk == 0:
      chk = a[i]
      ret = i
    elif chk < a[i]:
      chk = a[i]
      ret = i 

print(ret+1)



