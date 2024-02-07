n = int(input())
arr =list(map(int,input().split()))
dif = [0] * (n-1)

for i in range (n-1) :
    dif[i] = arr[i+1] - arr[i]
print(min(dif))