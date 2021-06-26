cont = ''
while cont != 'stop':
    n = int(input('Entre un nombre n: '))
    z = int(0)
    for i in range (2,n-1) :
        print(i)
        if n%i == 0:
            z = z+1

    if z == 0:
        print("premier")

    else:
        print("pas premier")

    cont = str(input())

#author Marc-Oliver Jufer
