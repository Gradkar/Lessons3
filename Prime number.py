print("Enter the number you would like to check")
a = int(input())
while(True):
    if a % 2 == 0:
        print("The number is not simple. Divided into 2")
        break
    else:
        if a % 3 == 0:
            print("The number is not simple. Divided into 3")
            break
        else:  
            if a % 5 == 0:
                print("The number is not simple. Divided into 5")
                break
            else:
                if a % 7 == 0:
                    print("The number is not simple. Divided into 7")
                    break
                else:
                    print("Prime number")
                    break
