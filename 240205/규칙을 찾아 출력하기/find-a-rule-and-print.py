n = int(input())

for i in range (1, n+1) :
    for j in range (1, n+1) :
        if i == 1 or i == n :
            print("*", end=" ")
        elif j < i :
            print("*", end = " ")
        elif j == n :
            print("*", end = " ")
        else :
            print(" ",end = " ")
    print("")