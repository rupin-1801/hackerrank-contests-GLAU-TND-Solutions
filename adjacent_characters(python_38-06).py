s = input()
if len(s) % 2 == 0:
    i = 0
    while(i < len(s)):
        temp = s[i:i+1]
        if i != 0:
            s = s[0:i] + s[i+1:len(s)]
        else:
            s = s[i+1:len(s)]
        s = s[0:i+1] + temp + s[i+1:len(s)]
        i+=2
    print(s)
else:
    print("Odd length.")
