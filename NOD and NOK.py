print("Enter the first number")
a = int(input())
print("Enter the second number")
b = int(input())
c = a*b  # Считаем произведение двух чисел.
while a != 0 and b != 0:  # Цикл работает пока числа не равны нулю.
    if a > b:  # Проверяем какой элемент больше.
        a = a % b  # Считаем остаток от деления.
    else:
        b = b % a  # Считаем остаток от деления.
print("NOD",a + b)
print("NOK",c/(a+b))