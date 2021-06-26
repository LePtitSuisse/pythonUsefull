import time   #normal
import random #normal
import os
import Compte_a_rebours #importe la classe que j'ai créer

c = Compte_a_rebours.Compte_a_rebours('Compte a rebours') #crée un objet 'c' avec comme attribut name='Compte a rebours' 

c.set_duree(5)    #éxécute la fonction set_duree sur l'objet c
c.go()
c.get_duree()
