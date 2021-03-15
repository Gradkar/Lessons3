factorial = lambda x: factorial(x - 1) * x if x > 1 else 1
print("Введите число, факториал которого будем считать")
a = input()
if (a.isdigit()):
    a = int(a)
    print("Факториал числа равен",factorial(a))
else:
    print("Попробуйте ввести число еще раз")