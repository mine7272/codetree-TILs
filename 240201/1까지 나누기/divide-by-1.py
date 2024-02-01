n = int(input())
i = 1
while(1) :
    if n//i <= 1 :
        break
    n //= i 
    i += 1
print(i)