a, b, c = map(int,input().split())

if a > b :
    if a < c : 
        print(a)
    elif b < c :
        print(c)
    else :
        print (b)
else :
    if b < c  :
        print(b) 
    elif a > c :
        print(a)
    else :
        print(c)