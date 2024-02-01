a, b, c= map(int,input().split())
RES = False

for i in range (a,b+1) :
    if i % c == 0 :
        RES = True

if RES == True :
    print("YES")
else :
    print("NO")