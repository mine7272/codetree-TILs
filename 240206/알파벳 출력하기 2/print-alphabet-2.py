n = int(input())
x = ord('A')
for i in range (0, n):
    for j in range (0,n):
        if j < i :
            print(" ",end = " ")
        else :
            print(chr(x),end = " ")
            x += 1
            if x > ord('Z') :
                x = ord('A')
    print("")