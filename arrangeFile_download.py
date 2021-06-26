import shutil
import os

location_py = '{}/Programmation/Python'.format(os.getcwd()) #crée une variable pour stocker le dossier dans lequel doit se trouver tous les fichiers .py
location_bat = '{}/Programmation/bat'.format(os.getcwd())
location_image = '{}/Marc-Olivier/images'.format(os.getcwd())
location_desktop = '{}'.format(os.getcwd())
location_video = '{}/Marc-Olivier'.format(os.getcwd())
location_latex = '{}/Programmation/Latex'.format(os.getcwd())

fichiers_py = os.listdir(location_py) #crée une variable pour stocker la liste des éléments se trouvant défà dans le dossier
fichiers_bat = os.listdir(location_bat)
fichiers_desktop = os.listdir(location_desktop)

for f in fichiers_desktop:
    if f.endswith('.py') and f != 'arrangeFile.py':
        shutil.move('{}/{}'.format(location_desktop, f),'{}'.format(location_py))
        print('Le fichier',f,'a bien été déplacé dans le dossier Phyton')
    else:
        pass

for f in fichiers_desktop:
    if f.endswith('.bat'):
        shutil.move('{}/{}'.format(location_desktop,f),'{}'.format(location_bat))
        print('Le fichier',f,'a bien été déplacé dans le dossier bat')
    else:
        pass

for f in fichiers_desktop:
    if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg') or f.endswith('.gif'):
        shutil.move('{}/{}'.format(location_desktop,f),'{}'.format(location_image))
        print('Le fichier',f,'a bien été déplacé dans le dossier images')

    else:
        pass

for f in fichiers_desktop:
    if f.endswith('.MP4'):
        shutil.move('{}/{}'.format(location_desktop,f),'{}'.format(location_video))
        print('Le fichier',f,'a bien été déplacé dans le dossier Marc-Olivier')

    else:
        pass

for f in fichiers_desktop:
    if f.endswith('.bib') or f.endswith('.aux') or f.endswith('.bbl') or f.endswith('.blg') or f.endswith('.log') or f.endswith('.out') or f.endswith('.pdf') or f.endswith('.gz') or f.endswith('.tex') or f.endswith('.toc'):
        shutil.move('{}/{}'.format(location_desktop,f),'{}'.format(location_latex))
        print('Le fichier',f,'a bien été déplacé dans le dossier Latex')

cont = input()
