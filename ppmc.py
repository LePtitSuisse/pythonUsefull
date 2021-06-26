i = bool(false)
u = 1

print("Bienvenue sur mon programme qui trouve le ppmc de deux nombre")

x = int(input("Entre un nombre x: "))
y = int(input("Entre un autre nombre y: "))


while i == false:
    if u%x == 0 and u%y == 0:
        print(u)
        i = true
    u = u+1

#author Marc-Olivier Jufer
