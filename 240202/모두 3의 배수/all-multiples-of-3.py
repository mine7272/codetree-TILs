res = True

for i in range (5) :
    n = int(input())
    if n % 3 != 0 :
        res = False

if res == False :
    print(0)
else :
    print (1)