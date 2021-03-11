print("Введите текст")
s = input()
d = dict()
for i in range(len(s)):
    if(d.get(s[i]) != None):
        d[s[i]] = d[s[i]] + 1
    else:
        d.update([(s[i], 1)])
l = list(d.keys())
for j in range(len(l)):
    print("Частота встречаемости символа", l[j])
    print(d[l[j]]/len(s))