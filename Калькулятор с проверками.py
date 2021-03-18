def summa(a,b):
    try: 
        int(a)
    except ValueError:
        print("Введите первое число еще раз")
    else:
        a = int(a)
    try: 
        int(b)
    except ValueError:
        print("Введите второе число еще раз")
    else:
        b = int(b)
    try:
        a + b
    except TypeError:
        print("Ошибка с типами переменных")
    except OverflowError:
        print("Возникло переполнение")
    else:
        print("Сумма двух чисел равна", a+b)
def razn(a,b):
    try: 
        int(a)
    except ValueError:
        print("Введите первое число еще раз")
    else:
        a = int(a)
    try: 
        int(b)
    except ValueError:
        print("Введите второе число еще раз")
    else:
        b = int(b)
    try:
        a - b
    except TypeError:
        print("Ошибка с типами переменных")
    except OverflowError:
        print("Возникло переполнение")
    else:
        print("Разница двух чисел равна", a-b)
def proz(a,b):
    try: 
        int(a)
    except ValueError:
        print("Введите первое число еще раз")
    else:
        a = int(a)
    try: 
        int(b)
    except ValueError:
        print("Введите второе число еще раз")
    else:
        b = int(b)
    try:
        a * b
    except TypeError:
        print("Ошибка с типами переменных")
    except OverflowError:
        print("Возникло переполнение")
    else:
        print("Произведение двух чисел равна", a*b)
def delet(a,b):
    try: 
        int(a)
    except ValueError:
        print("Введите первое число еще раз")
    else:
        a = int(a)
    try: 
        int(b)
    except ValueError:
        print("Введите второе число еще раз")
    else:
        b = int(b)
    try:
        a / b
    except TypeError:
        print("Ошибка с типами переменных")
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
    except OverflowError:
        print("Возникло переполнение")
    else:
        print("Деление превого числа на второе равно", a/b)
def step(a,b):
    try: 
        int(a)
    except ValueError:
        print("Введите первое число еще раз")
    else:
        a = int(a)
    try: 
        int(b)
    except ValueError:
        print("Введите второе число еще раз")
    else:
        b = int(b) 
    try:
        a ** b
    except TypeError:
        print("Ошибка с типами переменных")
    except OverflowError:
        print("Возникло переполнение")
    else:
        print("Произведение двух чисел равна", a**b)      
while(True):
    print("Введите первое число в калькулятор")
    a = input()
    print("Введите команду представленную из списка")
    print("Для суммирования чисел введите +")
    print("Для вычисления разности чисел введите -")
    print("Для перемножения чисел введите *")
    print("Для вычисления деления чисел введите /")
    print("Для возведения в степень одного из чисел введите ^")
    opr = input()
    print("Введите второе число в калькулятор")
    b = input()
    if opr == '+':
        summa(a,b)
    if opr == '-':
        razn(a,b)
    if opr == '*':
        proz(a,b)
    if opr == '/':
        delet(a,b)
    if opr == '^':
        step(a,b)
    print("Желаете продолжить работу с калькулятором ? Для продолжения работы введите Да")
    st = input()
    if st == '':
        break