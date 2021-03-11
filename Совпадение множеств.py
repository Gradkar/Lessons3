print("Введите числа для первого списка")
s = input()
print("Введите числа для первого списка")
t = input()
if(s.isdigit() and t.isdigit()):
    l = list()
    k = list()
    for i in range(len(s)):
        l.append(int(s[i]))
    for i in range(len(t)):
        k.append(int(s[i]))
    print(l)
    print(k)
    l = set(l)
    k = set(k)
    print(l)
    print(k)
    if(l == k):
        print("Множества элементов двух списков совпадают")
    else:
        print("Множества элементов двух списков не совпадают")
else:
    print("Введите числа для списко еще раз")