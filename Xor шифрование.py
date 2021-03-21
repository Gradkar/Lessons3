filename = ''
print("Введите название файла или нажмите Enter для использования файла по-умолчанию")
filename = input()
if (filename == ''):
    f = open("./text.txt","r")  # Открываем на чтение файл.
    st = f.read()  # Считываем весь текст в строку.
    f.close()  # Закрываем файл.
else:
    f = open(filename,"r")  # Открываем на чтение файл.
    st = f.read()  # Считываем весь текст в строку.
    f.close()  # Закрываем файл.
print("Enter the encryption key")
kl = input()
i = 0
rt = ""
while(i < len(st)):
    rt = rt + chr(ord(st[i])^ord(kl[i % len(kl)]))  # Сложение строки rt и символа зашифрованного XOR.
    i = i + 1
f = open("cript.txt","w")  # Открываем на запись файл.
f.write(rt)  # Записываем в файл строку rt.
f.close()  # Закрываем файл.