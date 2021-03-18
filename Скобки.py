stack = []
dictric = {'(': ')', '[': ']', '{': '}', '<': '>'}
flag = True
print("Введите текст для анализа скобок")
string = input()   
for symbol in string:
    if symbol in dictric.keys():
        stack.append(symbol)
    elif symbol in dictric.values():
        if stack:
            brak = stack.pop()
            if dictric.get(brak) != symbol:
                print("Ошибка")
                flag = False
                break
        else:
            print("Не пустой стек")
            flag = False
            break
if (flag == True):
    print("Скобки раставлены верно")
else:
    print("Скобки раставлены неверно")