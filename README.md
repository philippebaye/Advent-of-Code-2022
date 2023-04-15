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
    <tr><td><a href="day2">day2</a></td><td>15</td><td>14069</td><td>12</td><td>12411</td></tr>
    <tr><td><a href="day3">day3</a></td><td>157</td><td>7889</td><td>70</td><td>2825</td></tr>
    <tr><td><a href="day4">day4</a></td><td>2</td><td>547</td><td>4</td><td>843</td></tr>
    <tr><td><a href="day5">day5</a></td><td>CMZ</td><td>CVCWCRTVQ</td><td>MCD</td><td>CNSCZWLVT</td></tr>
    <tr><td><a href="day6">day6</a></td><td>7, 5, 6, 10, 11</td><td>1623</td><td>19, 23, 23, 29, 26</td><td>3774</td></tr>
    <tr><td><a href="day7">day7</a></td><td>95437</td><td>1086293</td><td>24933642</td><td>366028</td></tr>
 <tbody>
</table>
