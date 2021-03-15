def factorial(n):
    a = 1
    for i in range(2,n+1):
        a = a*i
    return a
while(True):
    print("Введите число, факториал которого будем считать")
    a = input()
    try:
        int(a)
    except ValueError:
        print("Введите число еще раз")
    else:
        a = int(a)
        print("Факториал числа равен",factorial(a))
        break