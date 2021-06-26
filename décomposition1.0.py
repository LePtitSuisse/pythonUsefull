cont = ''

while cont != 'stop':

    nombre = int(input('Entre un nombre n: '))
    div = 2

    while nombre != 1:


        z = int(0)
        for i in range (2,int(div**0.5)) :

            if div%i == 0:
                z = z+1

        if z == 0:
            if nombre%div == 0:
                print(div)
                nombre = nombre/div
            else:
                div = div+1

        else:
            div = div+1

    print('fini')
    cont = str(input())
