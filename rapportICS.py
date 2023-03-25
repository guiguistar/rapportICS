#!/usr/bin/env python3
# coding: utf-8

import sys
import os
import re
import arrow
from ics import Calendar
from collections import defaultdict

def convertirHHMMSSEnH(hhmmss : str) -> float:
    h, m, s = str(hhmmss).split(":")
    return float(h) + float(m) / 60 + float(s) / 3600

def afficherExemples():
    print('Exemples d\'utilisation :\n')
    print(' ./edt.py cal.ics 2023-02-17 2023-03-05')
    print(' ./edt.py cal.ics 2023-02-17')
    print(' ./edt.py cal.ics')
    print()
    print('Le nom du fichier .ics est obligatoire.')
    print('Si une seule date est donnée, elle est considérée comme la date de début de compte-rendu.')
    print('Si deux dates sont données, le programme affiche la liste de tous les événements s\'étant tenus entre ces deux dates.')

if __name__ == '__main__':
    nArgv = len(sys.argv)
    if nArgv < 2 :
        print('Il manque le nom du fichier.ics.')
        print()
        afficherExemples()
        exit()
    fichier = sys.argv[1]

    assert os.path.exists(fichier), f'Le fichier {fichier} n\'existe pas.'

    dateDebut = arrow.get('1970-01-01')
    dateFin   = arrow.get('3000-01-01')

    if nArgv >= 3:
        regex = re.compile('^\d{4}[/-]\d{2}[/-]\d{2}$')
        
        if regex.match(sys.argv[2]):
            print('La date de début fournie est valide.')
            dateDebut = arrow.get(sys.argv[2])

        if nArgv >= 4:
            if regex.match(sys.argv[3]):
                print('La date de fin fournie est valide.')
                dateFin = arrow.get(sys.argv[3])

    with open('cal.ics', 'r') as f:
        contenu = f.read()
        cal = Calendar(contenu)
        evs = list(cal.timeline)
        libelle = defaultdict(list)

    print(f'Date de début : {dateDebut}')
    print(f'Date de fin   : {dateFin}')

    totalHeures = 0

    for ev in evs:
        debut = ev.begin
        #print(str(debut), dateDebut <= debut <= dateFin)
        if dateDebut <= debut <= dateFin:
            c = ev.name
            d = ev.duration
            deb = ev.begin
            dEnFloat = convertirHHMMSSEnH(d)
            totalHeures += dEnFloat
            formatDate = 'DD-MM-YYYY à HH:mm'
            libelle[c].append( ( f'{dEnFloat}h', deb.format(formatDate, locale='fr') ) )
    
    for k,v in sorted(libelle.items()):
        for el in v:
            print(k[:50].ljust(50,'.'), *el)
            #print(el, k[:40].rjust(50,'.'))
    print(totalHeures)
