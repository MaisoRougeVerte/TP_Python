import time




entier = int(input("Rentrez un nombre positif : "))

while True:
    if entier < 0:
        entier = int(input("Rentrez à nouveau un nombre positif : "))
    elif entier == 0:
        break
    else:
        time.sleep(1)
        entier -= 1
        print(entier)
