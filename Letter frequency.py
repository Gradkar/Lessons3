print("Enter the text in English")
st = input()
d = dict([('a', 0), ('b', 0), ('c', 0), ('d', 0), ('e', 0), ('f', 0), ('g', 0), ('h', 0), ('i', 0), ('j', 0), ('k', 0), ('l', 0), ('m', 0),('n', 0), ('o', 0), ('p', 0), ('q', 0), ('r', 0), ('s', 0), ('t', 0), ('u', 0), ('v', 0), ('w', 0), ('x', 0), ('y', 0), ('z',0)])
kol_obs = 0
i = 0
st = st.lower()
while(i < len(st)):
    if(d.get(st[i]) != None):
            d[st[i]] = d[st[i]] + 1
            kol_obs = kol_obs + 1
    i = i + 1
print("Letter frequency a",d['a']/kol_obs)
print("Letter frequency b",d['b']/kol_obs)
print("Letter frequency c",d['c']/kol_obs)
print("Letter frequency d",d['d']/kol_obs)
print("Letter frequency e",d['e']/kol_obs)
print("Letter frequency f",d['f']/kol_obs)
print("Letter frequency g",d['g']/kol_obs)
print("Letter frequency h",d['h']/kol_obs)
print("Letter frequency i",d['i']/kol_obs)
print("Letter frequency j",d['j']/kol_obs)
print("Letter frequency k",d['k']/kol_obs)
print("Letter frequency l",d['l']/kol_obs)
print("Letter frequency m",d['m']/kol_obs)
print("Letter frequency n",d['n']/kol_obs)
print("Letter frequency o",d['o']/kol_obs)
print("Letter frequency p",d['p']/kol_obs)
print("Letter frequency q",d['q']/kol_obs)
print("Letter frequency r",d['e']/kol_obs)
print("Letter frequency s",d['s']/kol_obs)
print("Letter frequency t",d['t']/kol_obs)
print("Letter frequency u",d['u']/kol_obs)
print("Letter frequency v",d['v']/kol_obs)
print("Letter frequency w",d['w']/kol_obs)
print("Letter frequency x",d['x']/kol_obs)
print("Letter frequency y",d['y']/kol_obs)
print("Letter frequency z",d['z']/kol_obs)
