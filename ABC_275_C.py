import itertools

S =[]
for i in range(2):
  S.append(input())
ans = 0
for i1,j1,i2,j2 in itertools.product(range(9),repeat=4):
  if i2 > i1 & j2 >= j1 & S[i1][j1] == "#" & S[i2][j2] == "#":
    di = i2 - i1
    dj = j2 - j1
    i3 = i2 + dj
    j3 = j2 - di
    i4 = i3-di
    j4 = j3-dj

    if 0<=i3<9 and 0<=j3<9 and 0<=i4<9 and 0<=j4<9 and S[i3][j3]=="#" and S[i4][j4]=="#":
      ans+=1
print(ans)