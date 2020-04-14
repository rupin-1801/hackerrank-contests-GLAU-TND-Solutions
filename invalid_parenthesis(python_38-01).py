n=input()
left=0
right=0
for i in range(len(n)):
    if n[i]=='(':
        left=left+1
    if n[i]==')':
        right=right+1
if right!=left:
    v=False
else:
    v=True
print("'{}'".format(v))
