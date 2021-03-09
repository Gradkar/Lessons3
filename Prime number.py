print("Введите число, которое хотели бы проверить")
a = int(input())
while(True):
    if a % 2 == 0:
        print("Число не простое. Делится на 2")
        break
    else:
        if a % 3 == 0:
            print("Число не простое. Делится на 3")
            break
        else:  
            if a % 5 == 0:
                print("Число не простое. Делится на 5")
                break
            else:
                if a % 7 == 0:
                    print("Число не простое. Делится на 7")
                    break
                else:
                    print("Число простое")
                    break
