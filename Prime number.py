import math
print("Enter the number you would like to check")
a = input()
if(a.isdigit()):  # Проверяем состоят ли строки из цифр.
    pr = True
    a = int(a)
    for i in range(2,round(math.sqrt(a)) + 1):  # Запускаем цикл от 2 до корня из числа + 1.
        if(a % i == 0):  # Проверяем делится ли число на элемент i.
            pr = False
            break
    if pr:  # Проверяем флаг на простоту.
        print("Число простое")
    else:
        print("Число не простое")
else:
    print("Введите еще раз числоaa")