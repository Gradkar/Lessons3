import math
print("Enter the highest coefficient")
a = int(input())
print("Enter the lowest coefficient")
b = int(input())
print("Enter the free Coefficient")
c = int(input())
if a == 0:
    print("x",-c/b)
else:    
    if b == 0:
        if -c/a > 0:
            print("x1",math.sqrt(-c/a))
            print("x2",-math.sqrt(-c/a))
        if -c/a < 0:
            print("x1",complex(0,math.sqrt(abs(-c/a))))
            print("x1",complex(0,-math.sqrt(abs(-c/a))))
    else:
        Des = b*b - 4*a*c
        if Des == 0:
            print("x",-b/(2*a))
        if Des > 0:
            print("x1",(-b-math.sqrt(Des))/(2*a))
            print("x2",(-b+math.sqrt(Des))/(2*a))
        if Des < 0:
            print("x1",complex(-b/(2*a),math.sqrt(abs(Des))/(2*a)))
            print("x2",complex(-b/(2*a),-math.sqrt(abs(Des))/(2*a)))