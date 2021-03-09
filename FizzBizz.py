a = 0
while(a <= 100):
    t = ''
    if(a % 3 == 0):
        t = t + 'Fizz'
    if(a % 5 == 0):
        t = t + 'Bizz'
    print(t)
    a = a + 1