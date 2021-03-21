print("Endless traffic light.")
while(True):  # Запускается вечный цикл
    print("Enter the color of the traffic light (Red,Yellow and Green) or enter the Exit to stop the cycle.")
    svet = input()
    if svet == "Red":  # Проверяем какой свет светофора введен.
        print("Travel is prohibited!")
    if svet == "Yellow":
        print("Travel is prohibited. Attention get ready to start moving.")
    if svet == "Green":
        print("Travel is allowed.You can start moving now.")
    if svet == "Exit":  # Если введен Exit
        break
print("The traffic light has finished its work")