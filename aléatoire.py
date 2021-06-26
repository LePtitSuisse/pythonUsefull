import random
import time

print("Salut, bienvenue sur mon fantastique programme inutile")

z = int(0)
y = int(0)

while z == 0:
    y = int(0)
    print("Entre 'dé' pour lancer un dé")
    print("Entre 'nombre' pour tirer au sort un nombre")
    mode = str(input());
    if mode == "dé":
        while y<=4:
            print("Suspence")
            time.sleep(1)
            print(random.randrange(1,7))
            y = y+1
    elif mode == "nombre":
        while y<=4:
            poss = int(input("Entre le nombre le possibilité voulues : "))
            x = int(input("Entre le nombre de nombres tirés : "))
            for i in range (0,x):
                print("Suspence")
                time.sleep(1)
                print(random.randrange(1, poss+1))
            y = y+1

#author Marc-Olivier Jufer
