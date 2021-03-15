def vklad(vz,pr,n):
    a = vz
    for i in range(n+1):
        a = vz + a + a*pr/100
    return a
print("Введите размер ежемесячного взноса")
vz = input()
print("Введите процент по вкладу")
pr = input()
print("Введите количество месяцев, на которое был положен вклад")
n = input()
if(vz.isdigit() and pr.isdigit() and n.isdigit()):
    vz = int(vz)
    pr = int(pr)
    n = int(n)
    print(vklad(vz,pr,n))
else:
    print("Введите числа еще раз")