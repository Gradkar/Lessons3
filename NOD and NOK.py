print("Enter the first number")
a = int(input())
print("Enter the second number")
b = int(input())
c = a*b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print("NOD",a + b)
print("NOK",c/(a+b))