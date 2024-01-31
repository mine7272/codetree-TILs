age, gender = input().split()
age2, gender2 = input().split()
age, age2=int(age), int(age2)

print(1 if ((age or age2) >= 19) and ((gender or gender2) == "M") else 0)