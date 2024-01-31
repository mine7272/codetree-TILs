a, b= map(int,input().split())
i = 1
swi = 0
res = 0
now = a

if b > a : 
    while (now < b) :
        if swi == 0 :
            res += abs(now - (a+i))
            now = a+i
            swi = 1
        elif swi == 1 :
            res += abs(now - (a-i))
            now = a-i
            swi = 0
        i *=2
else : 
    while (now > b) :
        if swi == 0 :
            res += abs(now - (a+i))
            now = a+i
            swi = 1
        elif swi == 1 :
            res += abs(now - (a-i))
            now = a-i
            swi = 0
        i *=2

res = res - (now - b)
print(res)