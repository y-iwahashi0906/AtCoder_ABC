N,M = map(int, input().split())
l= [[] for _ in range(N)]
for _ in range(M):
    A,B= map(int, input().split())
    l[A-1].append(B)
    l[B-1].append(A)

for i, v in enumerate(l):
    v.sort()
    print(len(v), " ".join(v))
    
    


      
