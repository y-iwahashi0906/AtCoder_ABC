N = int(input())

l = {}
def f(a):
  if a == 0:
    return 1
  if a not in l:
    l[a] = f(a//2) + f(a//3)
  return l[a]
  
print(f(N))



