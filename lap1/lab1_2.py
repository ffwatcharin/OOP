str = input("Enter Strings: ")

upper = 0 
lower = 0

for i in str:
    if (i.isupper()) == True:
        upper += 1
    elif (i.islower()) == True:
        lower += 1

print(lower)
print(upper)