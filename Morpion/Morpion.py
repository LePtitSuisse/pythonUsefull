from random import randint
class Morpion:
    def __init__ (self):
        self.contenu = [1,2,3,4,5,6,7,8,9]
        self.victoire = False
        self.nul = False


    def print_tableau(self):
        print('|'+str(self.contenu[0])+'|'+str(self.contenu[1])+'|'+str(self.contenu[2])+'|')
        print('|'+str(self.contenu[3])+'|'+str(self.contenu[4])+'|'+str(self.contenu[5])+'|')
        print('|'+str(self.contenu[6])+'|'+str(self.contenu[7])+'|'+str(self.contenu[8])+'|')

    def coup(self, player, case):
        if player == True:
            num = 1
        else:
            num = 0
        self.contenu[case-1] = num

    def verification(self, player):
        c1 = self.contenu[0]
        c2 = self.contenu[1]
        c3 = self.contenu[2]
        c4 = self.contenu[3]
        c5 = self.contenu[4]
        c6 = self.contenu[5]
        c7 = self.contenu[6]
        c8 = self.contenu[7]
        c9 = self.contenu[8]
        if player == True:
            player = 'Joueur 1'
        else:
            player = 'Joueur 0'
        message_v = str(player+' a gagné')
        if c1 == c2 == c3 != '-':
            print(message_v)
            self.victoire = True
        elif c4 == c5 == c6 != '-':
            print(message_v)
            self.victoire = True
        elif c7 == c8 == c9 != '-':
            print(message_v)
            self.victoire = True
        elif c1 == c4 == c7 != '-':
            print(message_v)
            self.victoire = True
        elif c2 == c5 == c8 != '-':
            print(message_v)
            self.victoire = True
        elif c3 == c6 == c9 != '-':
            print(message_v)
            self.victoire = True
        elif c1 == c5 == c9 != '-':
            print(message_v)
            self.victoire = True
        elif c3 == c5 == c7 != '-':
            print(message_v)
            self.victoire = True
        c_remplies = 0
        for i in self.contenu:
            if i == '-':
                pass
            else:
                c_remplies = c_remplies+1
        if c_remplies == 9 and self.victoire == False:
            print('Match nul')
            self.nul = True

    def random_IA(self): #return case
        case = int(randint(1,9))
        while self.contenu[case-1] != '-':
            case = int(randint(1,9))
