from functools import reduce
def frequency(st):
    st = st.lower()
    d = dict()
    for i in range(len(st)):
        if(d.get(st[i]) != None):
            d[st[i]] = d[st[i]] + 1
        else:
            d.update([(st[i], 1)])
    l = list(d.keys())
    for j in range(len(l)):
        print("Частота встречаемости символа ", l[j])
        print(d[l[j]]/len(st))
def kol_predl(st):
    t = 0
    t = st.count("...")
    st = st.replace("...", ">")
    t = t + st.count(".")
    t = t + st.count("!")
    t = t + st.count("?")
    print("Количество предложений в тексте ",t)
def kol_slov(st):
    wordlist = st.split(' ')
    print("Количество слов в тексте ",len(wordlist))
print("Рассмотрим работу программы на примере строки")
st = "Все смешалось в доме Облонских? Жена узнала, что  муж  был  в  связи  с бывшею в их доме француженкою-гувернанткой, и объявила мужу,  что  не  может жить с ним в одном доме...  Положение  это  продолжалось  уже  третий  день  и мучительно чувствовалось и  самими  супругами,  и  всеми  членами  семьи,  и домочадцами! Все члены семьи и домочадцы чувствовали, что нет  смысла  в  их."
frequency(st)
kol_predl(st)
kol_slov(st)
