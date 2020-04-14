s = input()
s = " ".join(s)
x = 0
y = 0
l = list(s.split())
for i in  l:
    if i == "L":
        x-=1;
    elif i== "R":
        x+=1;
    elif i == "U":
        y+=1;
    elif i == "D":
        y-=1;
if x == 0 and y == 0:
    print("true")
else:
    print("false")
