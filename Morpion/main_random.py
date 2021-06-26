import Morpion
import time

m = Morpion.Morpion()
tableau = m.contenu

player = True
m.print_tableau()
m.contenu = ['-','-','-','-','-','-','-','-','-']
while m.victoire == False and m.nul == False:
    if player == True:
        case = int(input('Entre la case dans laquelle tu veux jouer: '))
        m.coup(player,case)
    else:
        case = m.random_IA
        m.coup(player,case)
    m.print_tableau()
    m.verification(player)
    player = not player
