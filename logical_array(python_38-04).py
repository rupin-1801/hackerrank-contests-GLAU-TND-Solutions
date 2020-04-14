n=list(map(int,input().split()))
max=0
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if max < (n[i]&n[j]):
            max = n[i]&n[j]
print(max)
