n = int(input())
arr = []

for i in range (n) :
    arr.append(int(input()))

for i in range (0,n) :
    if arr[i]%2 != 0 and arr[i]%3 == 0 :
        print(arr[i])