a = 0
while(a <= 100):  # Запускаем цикл от 0 до 100.
    t = ''
    if(a % 3 == 0):  # Проверяем делится ои чило на 3.
        t = t + 'Fizz'
    if(a % 5 == 0):  # Проверяем делится ои чило на 5.
        t = t + 'Bizz'
    print(t)
    a = a + 1