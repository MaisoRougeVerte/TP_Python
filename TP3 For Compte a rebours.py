import time


entier = int(input("Rentrez un nombre positif : "))

for i in range(entier):
    entier -= 1
    time.sleep(1)
    print(entier)