import os
import subprocess
import json
import re

def get_git_history(file_path):
    """ Ermittelt die Git-Historie für eine Datei. """
    history = subprocess.check_output(['git', 'log', '--format=%H|%an|%aI', '--', file_path]).decode().strip()
    return [line.split('|') for line in history.split('\n') if line]

def update_file_revision(file_path, history):
    """ Aktualisiert die Revisionsnummer einer Datei, falls notwendig. """
    revision_number = len(history)
    base_name, ext = os.path.splitext(file_path)
    # Entfernt die alte Revisionsnummer, falls vorhanden
    new_base_name = re.sub(r'-Rev\.\d+', '', base_name)
    # Fügt das neue Revisionspräfix hinzu
    new_file_name = f"{new_base_name}-Rev.{revision_number}{ext}"
    if file_path != new_file_name:
        os.rename(file_path, new_file_name)

def update_tracking_file(tracking_data, file_path, history):
    """ Aktualisiert die Tracking-Datei mit den neuesten Informationen. """
    if history:
        first_commit, last_commit = history[-1], history[0]
        tracking_data[file_path] = {
            'created_at': first_commit[2],
            'updated_at': last_commit[2],
            'creator': first_commit[1],
            'last_modifier': last_commit[1]
        }

# Hauptlogik
script_name = 'rename_files_with_revision.py'  # Name des Skripts, das ausgeschlossen werden soll
tracking_data = {}
exclude_dirs = ['.git', '.github', 'venv', '__pycache__']  # Ausschließende Verzeichnisse

for root, dirs, files in os.walk('.', topdown=True):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]  # Ausschluss bestimmter Verzeichnisse
    for name in files:
        if name == script_name:
            continue  # Ignoriere das Skript selbst
        file_path = os.path.join(root, name)
        history = get_git_history(file_path)
        update_file_revision(file_path, history)
        update_tracking_file(tracking_data, file_path, history)

# Speichern der Tracking-Informationen
with open('file_tracking.json', 'w') as f:
    json.dump(tracking_data, f, indent=4)
