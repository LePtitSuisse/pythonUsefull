import time
from random import *

f = open('dico2.txt')
dico = f.read()
dico = dico.splitlines()

def melange(mot):
    mot_melange = ''
    d = []
    for i in range(0,len(mot)):
        index = randint(0,(len(mot)-1))
        while index in d:
            index = randint(0,(len(mot)-1))
        mot_melange = mot_melange + mot[index]
        d.append(index)
    return(mot_melange)

def cache(mot):
    mot_cache = ''
    for i in mot:
        mot_cache = mot_cache + '_'
    return(mot_cache)

def print_mot_cache(mot_cache):
    mot_cache_espace = ''
    for i in mot_cache:
        mot_cache_espace = mot_cache_espace+i+' '
    print(mot_cache_espace)
    return(mot_cache_espace)

def autre():
    cont = ''
    while cont != 'stop':
        reponse = ''
        mot = dico[randint(0,(len(dico)-1))]
        print(melange(mot))
        while reponse != mot:
            reponse = str(input('Entre la réponse: '))
            if reponse == mot:
                print('Juste')
            elif reponse == '?':
                print(mot)
                reponse = mot
            else:
                print('Faux')
        cont = str(input())

def pendu():
    mot = dico[randint(0,(len(dico)-1))]
    lettre_essayee = []
    réponse = ''
    mot_cache = cache(mot)
    print(mot_cache)
    while réponse != mot:
        mode = str(input('Entre "lettre" pour demander une lettre et "mot" si tu as deviné le mot, et réponse si tu veux la connaitre:'))
        print('Ensuite, tape ENTER pour continuer et "q" pour revenir au choix du mode')
        if mode == 'lettre':
            cont = ''
            while cont != 'q':
                print(lettre_essayee)
                lettre = str(input('Entre une lettre: '))
                if lettre not in lettre_essayee:
                    lettre_essayee.append(lettre)
                for lettre in lettre_essayee:
                    for i in range(0,len(mot)):
                        if mot[i] == lettre:
                            mot_cache = mot_cache[:i] + lettre + mot_cache[i+1:]
                        else:
                            pass
                print_mot_cache(mot_cache)
                cont = str(input())
        elif mode == 'mot':
            cont = ''
            while cont != 'q':
                réponse = str(input('Entre le mot que tu pense être le bon: '))
                if réponse == mot:
                    print('juste')
                    cont = 'q'
                else:
                    print('faux')
                    cont = 'q'
                    réponse = mot
        elif mode == 'réponse':
            print(mot)
            réponse = mot


print('Salut, Bienvenue')
mode = str(input('Entre "pendu" pour jouer au pendu et "autre" pour un jeux moins difficile: '))
if mode == 'pendu':
    pendu()
elif mode == 'autre':
    autre()
