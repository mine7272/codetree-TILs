n = int(input())
res = False

for i in range (2, (n//2)+1) :
    if n % i == 0 :
        break
    elif i == n//2 :
        res = True

if res == True :
    print("N")
else :
    print ("C")