N,A,B = map(int, input().split())

ans = 0
for i in range(1, N+1):
  sum = 0
  check_num = i
  print(i)
  while check_num > 0:
    sum = sum + check_num % 10
    check_num = check_num // 10

  if A <= sum & sum <= B:
      ans = ans + i

print(ans)