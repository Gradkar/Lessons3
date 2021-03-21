print("Enter the text you want to encrypt")
st = input()
print("Enter the encryption key")
kl = input()
i = 0
rt = ''
while(i < len(st)):
    rt = rt + chr(ord(st[i])^ord(kl[i % len(kl)]))  # Сложение строки rt и символа зашифрованного XOR.
    i = i + 1
print("Encrypted text", rt)
i = 0
st = ''
while(i < len(rt)):
    st = st + chr(ord(rt[i])^ord(kl[i % len(kl)]))  # Сложение строки rt и символа расшифрованного XOR.
    i = i + 1
print("Decrypted text", st)
