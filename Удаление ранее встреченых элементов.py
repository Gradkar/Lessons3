print("Введите список для проверки")
st = input()
if st.isdigit():
    lis = list()
    for k in range(len(st)):
        lis.append(int(st[k]))
    print("Введеный список", lis)   
    for i in range(len(lis)):
        j = len(lis) - 1
        for j in range(len(lis) - 1, i, -1):
            if lis[i] == lis[j]:
                lis.pop(j)
    print("Итоговый список",lis)
else:
    print("Введите список еще раз")