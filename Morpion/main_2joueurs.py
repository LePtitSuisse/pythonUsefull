import Morpion
import time

m = Morpion.Morpion()
tableau = m.contenu

player = True
m.print_tableau()
m.contenu = ['-','-','-','-','-','-','-','-','-']
while m.victoire == False and m.nul == False:
    case = int(input('Entre la case dans laquelle tu veux jouer: '))
    while case > 9 or m.contenu[case-1] != '-':
        case = int(input('Entre une case valide: '))
    m.coup(player,case)
    m.print_tableau()
    m.verification(player)
    player = not player
time.sleep(2)
