n, m = map(int,input().split())
arr=[[0]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().split())
    arr[a-1][b-1] = a*b

for a in arr :
    for b in a :
        print(b,end=' ')
    print("")