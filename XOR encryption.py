print("Введите текст, который вы хотите зашифровать")
st = input()
print("Введите ключ для шифрования")
kl = input()
i = 0
rt = ''
while(i < len(st)):
    rt = rt + chr(ord(st[i])^ord(kl[i % len(kl)]))
    i = i + 1
print(rt)
i = 0
st = ''
while(i < len(rt)):
    st = st + chr(ord(rt[i])^ord(kl[i % len(kl)]))
    i = i + 1
print(st)
