import os

# Überprüfen, ob die VERSION-Datei existiert
if not os.path.isfile('VERSION'):
    print("VERSION file not found")
    exit(1)

# Lesen der Version aus der VERSION-Datei
with open('VERSION', 'r') as file:
    version = file.read().strip()

# Durchlaufen aller Dateien im aktuellen Verzeichnis (und Unterordnern)
for root, dirs, files in os.walk('.'):
    for name in files:
        if name.startswith('.'):
            continue  # Ignoriere versteckte Dateien und Ordner
        old_file_path = os.path.join(root, name)
        file_name, file_extension = os.path.splitext(name)
        new_file_name = f"{file_name}-{version}{file_extension}"
        new_file_path = os.path.join(root, new_file_name)
        
        # Umbenennen der Datei
        print(f"Umbenennen: {old_file_path} zu {new_file_path}")
        os.rename(old_file_path, new_file_path)
