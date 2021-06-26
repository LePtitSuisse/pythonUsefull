continu = ''
while continu != 'stop':
    nbre = str(input('Entre le nombre que tu veux convertir : '))
    i = 0
    ans = 0
    b = (len(nbre))-1

    while i<=b:
        if nbre[b-i] == '1':
            ans = ans+(2**i)

        i = i+1
    print(ans)
    continu = str(input())

#@author Marc-Olivier Jufer
#Last modification: 07.05.20
