n = int(input())

for _ in range (n):
    a,b =map(int,input().split())
    sum = 0
    if a % 2 == 1 :
        a += 1
    for i in range (a, b+1,2):
        sum += i
    print(sum)