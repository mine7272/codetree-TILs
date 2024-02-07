a, b = map(int,input().split())
arr = [0,0,0,0,0,0,0,0,0,0]
ans = 0

while(a > 1) :
    arr[a%b] += 1
    a = a//b

for i in range (len(arr)) : # 배열의 경우 그냥 arr 만 넣어서 반복 돌리기
    ans += arr[i]*arr[i] 

print(ans)