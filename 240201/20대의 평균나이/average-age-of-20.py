avg = 0.0
sum = 0
i = 1

while(1):
    age = int(input())
    if age//10 == 2 :
        sum += age
        avg = sum / i
    else : break
    i += 1;

print(f"{avg:.2f}")