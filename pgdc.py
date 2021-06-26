cont = ''
while cont != 'stop':
    x = int(input('Entre un nombre x: '))
    y = int(input('Entre un nombre y: '))

    ans = 0

    if x<y:
        i = y
    else:
        i = x

    while ans == 0:
        if x%i == 0 and y%i == 0:
            ans = i
        else:
            i = i-1
    print(ans)
    cont = str(input())

#author Marc-Olivier Jufer
