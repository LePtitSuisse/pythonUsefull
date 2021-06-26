import time
cont = ''
while cont != 'stop':
    m = float(input("Entre ta masse en kg : "))
    t = float(input("Entre ta taille en m : "))

    imc = m/(t*t)

    print("Calcul de l'imc")
    time.sleep(2)
    print("Ton imc est de : " , imc)


    if imc < 18.5 and imc >= 15 :
        print("Maigre")

    elif imc >= 18.5 and imc < 25 :
        print("Normal")

    elif imc >= 25 and imc < 30 :
        print("Excès pondéral")

    elif imc > 30 and imc < 35:
        print("Obèse")

    elif imc > 35:
        print("Très obèse. La va vraiment falloir faire quelque chose")

    cont = str(input())
