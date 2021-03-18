f = open("./text.txt","r")
st = f.read()
f.close()
freq = map(lambda x: {x: st.count(x)}, set(st))
freq_list = list(freq)
for item in freq_list:
    print(item)