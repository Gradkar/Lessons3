print("Enter the color of the traffic light(Red,Yellow or Green).")
svet = input()
if svet == "Red":  # Проверяем какой свет светофора введен.
    print("Travel is prohibited!")
if svet == "Yellow":
    print("Travel is prohibited. Attention get ready to start moving.")
if svet == "Green":
    print("Travel is allowed.You can start moving now.")
