S = input() 

ret = -1
for i in range(len(S)):
    if S[i] == "a":
        ret = i

print(ret+1)

