import math
print("Enter the highest coefficient")
a = int(input())
print("Enter the lowest coefficient")
b = int(input())
print("Enter the free Coefficient")
c = int(input())
if a == 0:  # Проверяем равен ли нулю главный коэффицент.
    print("x",-c/b)  # Печатаем корень уравнения.
else:    
    if b == 0:  # Проверяем равен ли нулю низший коэффицент.
        if -c/a > 0:  # Проверяем какой знак у даного элемента.
            print("x1",math.sqrt(-c/a))  # Печатаем корень уравнения.
            print("x2",-math.sqrt(-c/a))  # Печатаем корень уравнения.
        if -c/a < 0:  # Проверяем какой знак у даного элемента.
            print("x1",complex(0,math.sqrt(abs(-c/a))))  # Печатаем комплексный корень уравнения.
            print("x1",complex(0,-math.sqrt(abs(-c/a))))  # Печатаем комплексный корень уравнения.
    else:
        Des = b*b - 4*a*c  # Вычисляем дискриминант.
        if Des == 0:  # Проверяем равен ли нулю дискриминант.  
            print("x",-b/(2*a))
        if Des > 0:  # Проверяем знак дискриминанта.
            print("x1",(-b-math.sqrt(Des))/(2*a))  # Печатаем корень уравнения.
            print("x2",(-b+math.sqrt(Des))/(2*a))  # Печатаем корень уравнения.
        if Des < 0:  # Проверяем знак дискриминанта.
            print("x1",complex(-b/(2*a),math.sqrt(abs(Des))/(2*a)))  # Печатаем комплексный корень уравнения.
            print("x2",complex(-b/(2*a),-math.sqrt(abs(Des))/(2*a)))  # Печатаем комплексный корень уравнения.