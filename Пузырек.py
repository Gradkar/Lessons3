def sorter(arr):
    for k in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("Введите числа для первого списка")
s = input()
if(s.isdigit()):
    l = list()
    for i in range(len(s)):
        l.append(int(s[i]))
    print("Исходный список",l)
    print("Отсортированный список", sorter(l))  
else:
    print("Введите числа для списков еще раз")