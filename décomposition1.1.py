cont = ''
l = [1]
maxl= max(l)

while cont != 'stop' :

    nombre = int(input("Entre un nombre n: "))
    div = 2

    while nombre != 1 :
        if nombre > maxl:

            z = int(0)
            for i in range (2,div-1) :
                if div%i == 0:
                    z = z+1

            if z == 0:
                l = l + [div]
                maxl = max(l)
                div = div+1

            else:
                div = div+1

        else :
            div = 2
            while nombre != 1:
                if nombre%div == 0:
                    nombre = nombre/div
                    print(div)
                else:
                    div = div+1

    #print(l)
    print('fini')
    cont = str(input('Enter stop to stop the program : '))

#author Marc-Olivier Jufer
