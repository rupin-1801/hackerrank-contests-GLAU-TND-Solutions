n=int(input())
m=int(input())
for i in range(n):
    for j in range(n-(i+1)):
        print(" ",end="")
        k=j
    for j in range(k+1,k+(2*i)+2):
        if i!=(m-1):
            if j==k+1 or j==k+(2*i)+1:
                print("*",end="")
            else:
                print(" ",end="")
        else:
            print("*",end="")
    print("")
