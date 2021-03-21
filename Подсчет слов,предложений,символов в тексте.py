from functools import reduce

def frequency(st):
    """С помощью данной функции считаем частоту вхождения букв в тексте.
    Аргументы, получаемые на вход:
    st - string, строка содержащая в себе текст, в котором надо подсчитать частоту вхождения букв в текст.
    В результате выполнения функции выводим частоту вхождения каждой буквы в тексте.
    """
    st = st.lower()  # Опускаем все буквы в нижний регистр.
    d = dict()  # Создаем словарь, в котором роль ключа отдается буквам, а значение выступает количество появлений в строке.
    for i in range(len(st)):  # Запускаем цикл от 0 до длины строки.
        if(d.get(st[i]) != None):  # Проверяем если такой ключ в словаре.
            d[st[i]] = d[st[i]] + 1  # Увеличиваем значение, если такой ключ есть.
        else:
            d.update([(st[i], 1)])  # Добавляем в словарь новую пару ключ-значение, если такого ключа нет.
    l = list(d.keys())  # Создаем лист ключей из словаря.
    for j in range(len(l)):  # Запускаем цикл от 0 до длины листа с ключами.
        print("Частота встречаемости символа ", l[j])
        print(d[l[j]]/len(st))  # Выводим частоту встречаемости буквы.


def kol_predl(st):
    """С помощью данной функции считаем количество предложений в тексте.
    Аргументы, получаемые на вход:
    st - string, строка содержащая в себе текст, в котором надо подсчитать количество предложений.
    В результате выполнения функции выводим количество предложений в тексте.
    """
    t = st.count("...")  # Присваеваем переменной количество вхождений троеточия в строку st.
    st = st.replace("...", ">")  # Заменяем троеточие на знак >.
    t = t + st.count(".")  # Прибовляем к результату количество вхождений точки в текст.
    t = t + st.count("!")  # Прибовляем к результату количество вхождений знака восклицаниыя в тексте.
    t = t + st.count("?")  # Прибовляем к результату количество вхождений знака вопроса в тексте.
    print("Количество предложений в тексте ",t)


def kol_slov(st):
    """С помощью данной функции считаем количество слов в тексте.
    Аргументы, получаемые на вход:
    st - string, строка содержащая в себе текст, в котором надо подсчитать количество слов.
    В результате выполнения функции выводим количество слов в тексте.
    """
    wordlist = st.split(' ')  # Разбиваем строку с текстом на пробелы.
    print("Количество слов в тексте ",len(wordlist))


print("Рассмотрим работу программы на примере строки")
st = "Все смешалось в доме Облонских? Жена узнала, что  муж  был  в  связи  с бывшею в их доме француженкою-гувернанткой, и объявила мужу,  что  не  может жить с ним в одном доме...  Положение  это  продолжалось  уже  третий  день  и мучительно чувствовалось и  самими  супругами,  и  всеми  членами  семьи,  и домочадцами! Все члены семьи и домочадцы чувствовали, что нет  смысла  в  их."
frequency(st)  # Вызываем выполнение функции на подсчет частоты вхождения букв в текст.
kol_predl(st)  # Вызываем выполнение функции на подсчет количества предложений в тексте.
kol_slov(st)  # Вызываем выполнение функции на подсчет количества слов в тексте.
