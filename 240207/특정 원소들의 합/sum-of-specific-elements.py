arr = []
res = 0

for _ in range (4) :
    arr.append(list(map(int,input().split())))

for i in range(4) :
    for j in range(4) :
        if i >= j :
            res += arr[i][j]

print(res)