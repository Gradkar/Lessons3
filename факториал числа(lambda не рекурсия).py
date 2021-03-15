from functools import reduce
def factorial(n):
    return reduce(lambda x,y: x*y, range(1,n+1))
print("Введите число, факториал которого будем считать")
a = input()
if(a.isdigit()):
    a = int(a)   
    print("Факториал числа равен",factorial(a))
else:
    print("Попробуйте ввести число еще раз")