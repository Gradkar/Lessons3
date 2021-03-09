print("Введите первое число")
a = int(input())
print("Введите второе число")
b = int(input())
c = a*b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print("NOD",a + b)
print("NOK",c/(a+b))