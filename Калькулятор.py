summ = lambda a,b: a+b
proz = lambda a,b: a*b
raz = lambda a,b: a-b
delen = lambda a,b: a/b
step = lambda a,b: a**b
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
    if(a.isdigit() and b.isdigit()):
        a = int(a)
        b = int(b)
        if opr == '+':
            print("",summ(a,b))
        if opr == '-':
            print("",raz(a,b))
        if opr == '*':
            print("",proz(a,b))
        if opr == '/':
            print("",delen(a,b))
        if opr == '^':
            print("",step(a,b))
    else:
        print("Введите числа еще раз")
    print("Желаете продолжить работу с калькулятором ? Для продолжения работы введите Да")
    st = input()
    if st == '':
        break