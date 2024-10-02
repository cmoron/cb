# Coding Battle Helper

Ce projet fournit un outil Python simple pour créer rapidement des répertoires et des fichiers avec un modèle de code de base pour les compétitions de programmation (coding battles).

## Installation

Pour installer l'outil en mode développement ou production, exécutez l'une des commandes suivantes à la racine du projet.

### Mode Développement (recommandé pour tester les modifications)

```bash
pip install -e .
```

### Mode Production

```bash
pip install .
```

## Utilisation

Une fois installé, l'outil cb sera disponible en ligne de commande.

### Créer un exercice

Pour créer un répertoire avec un fichier Python pour un exercice spécifique, utilisez la commande suivante :

```bash
cb <exercise_number>
```

Par exemple, pour créer un exercice 1 :

```bash
cb 1
```

Cela génèrera :

- Un répertoire 1/
- Un fichier 1.py avec le modèle de code suivant :

```python

#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

# Write your solution here
```

Le fichier .py sera également exécutable.

## Licence

Ce projet est sous licence MIT. Vous pouvez librement l'utiliser, le modifier et le distribuer.
