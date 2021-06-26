from matplotlib import pyplot

l = int(input("Entre l: "))
n = 1
tot = 0

list_n = []
list_tot = []

while True:
    x = (1/n)*l
    tot = tot + x
    list_n.append(n)
    list_tot.append(tot)
    if n%(10**4) == 0:
        print(n,tot)
    n = n+1

    if n == 10**7:
        break

pyplot.plot(list_n, list_tot)
pyplot.show()
