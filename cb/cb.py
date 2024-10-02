"""
Crée un répertoire et un fichier .py pour un exercice donné.

Usage:
    cb <exercise_number>
"""
import os
import sys

TEMPLATE = '''#!/usr/bin/env python3
#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\\n'))

# Write your solution here
'''

def create_exercise(exercise_number):
    """
    Crée un répertoire et un fichier .py pour un exercice donné.

    Args:
        exercise_number (str): Le numéro de l'exercice à créer.
    """
    directory = str(exercise_number)
    file_name = f"{exercise_number}.py"

    # Créer le répertoire
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Créer le fichier .py
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(TEMPLATE)

        # Rendre le fichier exécutable
        os.chmod(file_path, 0o755)
        print(f"Created {file_path}")
    else:
        print(f"{file_path} already exists.")

def main():
    """
    Fonction principale.
    """
    if len(sys.argv) != 2:
        print("Usage: cb <exercise_number>")
        sys.exit(1)

    exercise_number = sys.argv[1]
    create_exercise(exercise_number)
