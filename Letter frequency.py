print("Enter the text in English")
st = input()
d = dict(
        [('a', 0), ('b', 0), ('c', 0), 
        ('d', 0), ('e', 0), ('f', 0), 
        ('g', 0), ('h', 0), ('i', 0), 
        ('j', 0), ('k', 0), ('l', 0), 
        ('m', 0),('n', 0), ('o', 0), 
        ('p', 0), ('q', 0), ('r', 0), 
        ('s', 0), ('t', 0), ('u', 0), 
        ('v', 0), ('w', 0), ('x', 0), 
        ('y', 0), ('z',0)])  # Создаем словарь, где клю это буква.
kol_obs = 0
i = 0
st = st.lower()  # Опускаем строку в нижний регистр
while(i < len(st)):  # Запукаем цикл от 0 до длины строки
    if(d.get(st[i]) != None):  # Проверяем если такой ключ в словаре.
            d[st[i]] = d[st[i]] + 1  # Увеличиваем значение, если такой ключ есть.
            kol_obs = kol_obs + 1  # Увеличиваем значение общего числа букв в тексте.
    i = i + 1
l = list(d.keys())  # Создаем лист ключей из словаря.
for j in range(len(l)):  # Запускаем цикл от 0 до длины листа с ключами.
    print("Частота встречаемости символа", l[j])
    print(d[l[j]]/len(st))
