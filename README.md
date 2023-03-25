# Lisez-moi

## Utilisation

Exemples d'utilisation :

 ./edt.py cal.ics 2023-02-17 2023-03-05
 ./edt.py cal.ics 2023-02-17
 ./edt.py cal.ics
 ./edt.py cal.ics 2023-02-17 2023-03-05 TG

Le nom du fichier .ics est obligatoire.
Si une seule date est donnée, elle est considérée comme la date de début de compte-rendu.
Si deux dates sont données, le programme affiche la liste de tous les événements s'étant tenus entre ces deux dates.
Si, en plus des deux dates, une expression régulière est fournie, cette dernière est utilisée pour filtrer les résultats.

## Exemple de sortie :

```
La date de début fournie est valide.
La date de fin fournie est valide.
Expression réulière fournie : fondamentales.
Date de début : 2023-03-01T00:00:00+00:00
Date de fin   : 2023-04-01T00:00:00+00:00
TD_SUP_LI_G1 - Mathématiques fondamentales 2............ 1.5h 01-03-2023 à 12:30
TD_SUP_LI_G1 - Mathématiques fondamentales 2............ 1.5h 08-03-2023 à 12:30
TD_SUP_LI_G1 - Mathématiques fondamentales 2............ 1.5h 15-03-2023 à 12:30
TD_SUP_LI_G1 - Mathématiques fondamentales 2............ 1.5h 22-03-2023 à 12:30
TD_SUP_LI_G1 - Mathématiques fondamentales 2............ 1.5h 29-03-2023 à 11:30
TD_SUP_LI_G2 - Mathématiques fondamentales 2............ 1.5h 01-03-2023 à 14:00
TD_SUP_LI_G2 - Mathématiques fondamentales 2............ 1.5h 08-03-2023 à 14:00
TD_SUP_LI_G2 - Mathématiques fondamentales 2............ 1.5h 15-03-2023 à 14:00
TD_SUP_LI_G2 - Mathématiques fondamentales 2............ 1.5h 22-03-2023 à 14:00
TD_SUP_LI_G2 - Mathématiques fondamentales 2............ 1.5h 29-03-2023 à 13:00
TG - Mathématiques fondamentales 2...................... 1.5h 07-03-2023 à 12:00
TG - Mathématiques fondamentales 2...................... 1.5h 14-03-2023 à 12:00
TG - Mathématiques fondamentales 2...................... 1.5h 21-03-2023 à 12:00
TG - Mathématiques fondamentales 2...................... 1.5h 28-03-2023 à 11:00
21.0
```