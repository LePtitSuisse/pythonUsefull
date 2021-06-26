continu = ''
while continu != 'stop':

    nbre = int(input("Write the number you want to convert in binary: "))

    nbreOfBits = int(0)


    while 2**nbreOfBits <= nbre:     #choose the optimal number of bits
        nbreOfBits = nbreOfBits+1



    ans = str()                     #ans : answer

    while nbreOfBits >= 0:

        if (nbre-2**nbreOfBits) < 0:
            if ans == "":
                ans = ans           #avoid unnecessary zero

            else:
                ans = ans + "0"

        else:
            nbre = nbre-(2**nbreOfBits)
            ans= ans + "1"


        nbreOfBits = nbreOfBits-1

    print(ans)
    continu = str(input())
#@author Marc-Olivier Jufer
#Last modification: 07.05.20
