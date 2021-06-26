import time   #parce que il faut toujours
import random #pareil
import os
class Compte_a_rebours:   #crée la class "Compte_a_rebours", avec un vrai nom

######################################################################################
#fonction pour créer un objet (y'a deux '_' à côté de 'init'):
    def __init__(self, name):
        self.name = name
        self.duree = 10
######################################################################################

    def set_duree(self,duree): #fonction pour modifier la duree du compte à rebours
        self.duree = duree
    def go(self): #fonction pour lancer le compte à rebours
        for i in range (self.duree,-1,-1):
            print(i)                        #je pense tu comprends
            time.sleep(0.1)
    def get_duree(self):
        print(self.duree)
        os.system('sudo shutdown -h now')
        os.system('shutdown -s -t 010')
