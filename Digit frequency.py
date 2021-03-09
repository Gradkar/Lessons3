print("Введите первое число интервала")
a = int(input())
print("Введите второе число интервала")
b = int(input())
d = dict([(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0),])
if(a == 0):
    d[0] = 1
while(a <= b):
    c = a
    while(c > 0):
        if(d.get(c % 10) != None):
            d[c % 10] = d[c % 10] + 1
            c = c // 10
    a = a + 1
kol_obsh = d[0] + d[1] + d[2] + d[3] + d[4] + d[5] + d[6] + d[7] + d[8] + d[9]
print("Частота цифры 0", d[0]/kol_obsh)
print("Частота цифры 1", d[1]/kol_obsh)
print("Частота цифры 2", d[2]/kol_obsh)
print("Частота цифры 3", d[3]/kol_obsh)
print("Частота цифры 4", d[4]/kol_obsh)
print("Частота цифры 5", d[5]/kol_obsh)
print("Частота цифры 6", d[6]/kol_obsh)
print("Частота цифры 7", d[7]/kol_obsh)
print("Частота цифры 8", d[8]/kol_obsh)
print("Частота цифры 9", d[9]/kol_obsh)
