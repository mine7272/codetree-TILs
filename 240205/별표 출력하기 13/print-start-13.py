n = int(input())
num1 = 1
num2 = n

for i in range (1, (n*2)+1 ) :
    if i % 2 == 0 :
        for _ in range (num1) :
            print("*",end=' ')
        num1 += 1
        print("")
    else :
        for _ in range (num2) :
            print("*",end=' ')
        num2 -= 1
        print("")