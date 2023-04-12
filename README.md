# Advent of Code 2022

J'ai profité des énigmes proposées par [Advent of Code 2022](https://adventofcode.com/2022) pour m'initier à Python. De fait les scripts réalisés dans ce cadre sont naïfs et largement perfectibles.


## Organisation du repo

Les différentes éléments d'un jour sont regroupés dans un même répertoire dans lequel on peut trouver :
| Suffixe | Description
| - | -
| `_input.txt`        | Données fournies associées à l'énigme du jour
| `_input_sample.txt` | Données utilisées dans l'exemple
| `_part1.py`         | Script utilisé pour résoudre la partie 1
| `_part2.py`         | Script utilisé pour résoudre la partie 2

Les scripts sont écrits pour fonctionner en python3.

Si `SAMPLE` est présent dans les arguments, le script utilise pour les données le fichier `_input_sample.txt`, sinon il utilise le fichier `_input.txt` :
```bash
# Lancement du script correspondant à la partie 1 du jour 1, en utilisant les données de l'exemple (i.e. day1_input_sample.txt)
pyhton3 day1_part1.py SAMPLE

# Lancement du script correspondant à la partie 1 du jour 1, en utilisant les données de l'énigme à résoudre (i.e. day1_input.txt)
pyhton3 day1_part1.py
```


## Réponses

<table>
 <thead>
    <tr><th rowspan=2>Jour</th><th colspan=2 center>Partie 1</th><th colspan=2>Partie 2</th></tr>
    <tr><th>Exemple</th><th>Puzzle</th><th>Exemple</th><th>Puzzle</th></tr>
 </thead>
    <tr><td><a href="day1">day1</a></td><td>24000</td><td>74394</td><td>45000</td><td>212836</td></tr>
 <tbody>
</table>
