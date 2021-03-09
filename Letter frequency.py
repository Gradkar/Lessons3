print("Введите текст на английском языке")
st = input()
d = dict([('a', 0), ('b', 0), ('c', 0), ('d', 0), ('e', 0), ('f', 0), ('g', 0), ('h', 0), ('i', 0), ('j', 0), ('k', 0), ('l', 0), ('m', 0),('n', 0), ('o', 0), ('p', 0), ('q', 0), ('r', 0), ('s', 0), ('t', 0), ('u', 0), ('v', 0), ('w', 0), ('x', 0), ('y', 0), ('z',0)])
kol_obs = 0
i = 0
while(i < len(st)):
    if(d.get(st[i]) != None):
            d[st[i]] = d[st[i]] + 1
            kol_obs = kol_obs + 1
    i = i + 1
print("Частота буквы a",d['a']/kol_obs)
print("Частота буквы b",d['b']/kol_obs)
print("Частота буквы c",d['c']/kol_obs)
print("Частота буквы d",d['d']/kol_obs)
print("Частота буквы e",d['e']/kol_obs)
print("Частота буквы f",d['f']/kol_obs)
print("Частота буквы g",d['g']/kol_obs)
print("Частота буквы h",d['h']/kol_obs)
print("Частота буквы i",d['i']/kol_obs)
print("Частота буквы j",d['j']/kol_obs)
print("Частота буквы k",d['k']/kol_obs)
print("Частота буквы l",d['l']/kol_obs)
print("Частота буквы m",d['m']/kol_obs)
print("Частота буквы n",d['n']/kol_obs)
print("Частота буквы o",d['o']/kol_obs)
print("Частота буквы p",d['p']/kol_obs)
print("Частота буквы q",d['q']/kol_obs)
print("Частота буквы r",d['e']/kol_obs)
print("Частота буквы s",d['s']/kol_obs)
print("Частота буквы t",d['t']/kol_obs)
print("Частота буквы u",d['u']/kol_obs)
print("Частота буквы v",d['v']/kol_obs)
print("Частота буквы w",d['w']/kol_obs)
print("Частота буквы x",d['x']/kol_obs)
print("Частота буквы y",d['y']/kol_obs)
print("Частота буквы z",d['z']/kol_obs)
