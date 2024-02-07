a, b = map(int,input().split())
arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ans = 0

while(a >= 1) :
    arr[a%b] += 1
    a = a//b

for i in range (len(arr)) :
    ans += arr[i]*arr[i] 

print(ans)