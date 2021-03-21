filename = ''
print("Введите название файла или нажмите Enter для использования файла по-умолчанию")
filename = input()
if (filename == ''):
    f = open("cript.txt","r")  # Открываем на чтение файл.
    st = f.read()  # Считываем весь текст в строку.
    f.close()  # Закрываем файл.
else:
    f = open(filename,"r")  # Открываем на чтение файл.
    st = f.read()  # Считываем весь текст в строку.
    f.close()  # Закрываем файл.
print("Enter the encryption key")
kl = input()
i = 0
rt = ""  # Создаем результирующую строку
while(i < len(st)):  # Запускаем цикл с нуля до длины строки
    rt = rt + chr(ord(st[i])^ord(kl[i % len(kl)]))  # Сложение строки rt и символа расшифрованного XOR.
    i = i + 1
f = open("ancript.txt","w")  # Открываем на запись файл.
f.write(rt)  # Записываем в файл строку rt.
f.close()  # Закрываем файл.