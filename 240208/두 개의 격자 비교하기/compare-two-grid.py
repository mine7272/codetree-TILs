a, b= map(int,input().split())
arr1 = []
arr2 = []
ans = [[0]*b]*a

for _ in range (a) :
    arr1.append(list(map(int,input().split())))

for _ in range (a) :
    arr2.append(list(map(int,input().split())))

for i in range (a):
    for j in range(b):
        if arr1[i][j] == arr2[i][j] :
            ans[i][j] = 0
        else : 
            ans[i][j] = 1
        print(ans[i][j],end=' ')
    print("")