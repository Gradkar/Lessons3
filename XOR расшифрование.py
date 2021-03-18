filename = ''
print("Введите название файла или нажмите Enter для использования файла по-умолчанию")
filename = input()
if (filename == ''):
    f = open("cript.txt","r")
    st = f.read()
    f.close()
else:
    f = open(filename,"r")
    st = f.read()
    f.close()
print("Enter the encryption key")
kl = input()
i = 0
rt = ""
while(i < len(st)):
    rt = rt + chr(ord(st[i])^ord(kl[i % len(kl)]))
    i = i + 1
f = open("ancript.txt","w")
f.write(rt)
f.close()