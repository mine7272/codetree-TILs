n = int(input())

for i in range(n,0,-1) :
    for j in range(1,n+1) :
        if j <= i :
            print("*",end='')
        else :
            print(" ",end='')
    for j in range(n,0,-1) :
        if j <= i :
            print("*",end='')
        else :
            print(" ",end='')
    print("")