f = open("./text.txt","r")  # Открываем на чтение файл.
st = f.read()  # Считываем весь текст в строку.
f.close()  # Закрываем файл.
freq = map(lambda x: {x: st.count(x)}, set(st)) # Подсчитываем частоту вхождения букв в текст.
freq_list = list(freq)  # Создаем лист частот
for item in freq_list:
    print(item)