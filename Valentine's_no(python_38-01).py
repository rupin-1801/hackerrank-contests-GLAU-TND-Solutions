s=input()
l=s.split(",")
l=list(map(int,l))
x=l[0]
y=l[1]
if (x^y) == (x+y):
    print("'Valentine Match'")
else:
    print("None")
