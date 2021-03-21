print("Enter the first number of the interval")
a = int(input())
print("Enter the second number of the interval")
b = int(input())
d = dict([(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0),])  # Создаем словарь.
if(a == 0):
    d[0] = 1
while(a <= b):  # Запускаем цикл пока элемент a меньше b.
    c = a
    while(c > 0):  # Запускаем цикл пока элемент c больше 0.
        if(d.get(c % 10) != None):  # Проверяем остаток от деления.
            d[c % 10] = d[c % 10] + 1  # Увеличиваем значение для цифры.
            c = c // 10  # Получаем целую часть.
    a = a + 1
kol_obsh = d[0] + d[1] + d[2] + d[3] + d[4] + d[5] + d[6] + d[7] + d[8] + d[9]  # Подсчет общего количества элементов.
print("Digit frequency 0", d[0]/kol_obsh)
print("Digit frequency 1", d[1]/kol_obsh)
print("Digit frequency 2", d[2]/kol_obsh)
print("Digit frequency 3", d[3]/kol_obsh)
print("Digit frequency 4", d[4]/kol_obsh)
print("Digit frequency 5", d[5]/kol_obsh)
print("Digit frequency 6", d[6]/kol_obsh)
print("Digit frequency 7", d[7]/kol_obsh)
print("Digit frequency 8", d[8]/kol_obsh)
print("Digit frequency 9", d[9]/kol_obsh)
