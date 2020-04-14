s=int(input())
m=len(str(bin(s)))
for i in range(s+1):
    s1=str(bin(i))
    for i in range(m-len(s1)):
        print(" ",end="")
    print(s1[2:])
