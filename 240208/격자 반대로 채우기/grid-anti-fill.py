n = int(input())
arr = [[0] * n for _ in range(n)]
su = 1
updown = True

for i in range (n-1,-1,-1) :
    if updown == True :
        for j in range (n-1, -1,-1) :
            arr[j][i] = su
            su += 1
        updown = False
    else : 
        for j in range (0,n) :
            arr[j][i] = su
            su += 1
        updown = True


for a in arr :
    for b in a :
        print(b,end=' ')
    print('')