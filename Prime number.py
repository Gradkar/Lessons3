import math
print("Enter the number you would like to check")
a = input()
if(a.isdigit()):
    pr = True
    a = int(a)
    for i in range(2,round(math.sqrt(a)) + 1):
        if(a % i == 0):
            pr = False
            break
    if(pr == True):
        print("Число простое")
    else:
        print("Число не простое")
else:
    print("Введите еще раз число")