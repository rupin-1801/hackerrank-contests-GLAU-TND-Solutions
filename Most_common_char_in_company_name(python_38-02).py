s=input()
j=0
l=[]
dic={}
for i in range(97,123):
    dic[i]=s.count(chr(i))
for i in range(3):
    d=max(dic,key=dic.get)
    l.append([])
    l[i].append(chr(d))
    l[i].append(dic[d])
    dic[d]=0
for i in l:
    print(i[0],i[1])
