l1={}
d=[]
l=list(input().split(","))
for i in l:
    s=0
    for j in l:
        if i==j:
            s+=1
        l1[i]=s
k=0
for i in l1:
    if k>l1[max(l1,key=l1.get)]:
        break
    else:
        maxm=max(l1,key=l1.get)
        d.append(maxm)
        k=l1[maxm]
        l1[maxm]=0
d=sorted(d)
print(d[0])
