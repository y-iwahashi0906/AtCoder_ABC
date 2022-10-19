N = int(input())
a = list(map(int, input().split()))

ans = 0
alice = 0
bob = 0
a.sort(reverse=True)
print(a)

for i in range(N):
  if i % 2 == 0:
    alice += + a[i]
  else:
    bob += + a[i]


print(alice - bob)