import os
import subprocess

def get_last_commit_id(file_path):
    try:
        commit_id = subprocess.check_output(['git', 'log', '-n', '1', '--pretty=format:%h', '--', file_path]).decode().strip()
        return commit_id
    except subprocess.CalledProcessError:
        return None

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.startswith('.') or root.startswith('./.github/workflows'):
            continue
        file_path = os.path.join(root, name)
        commit_id = get_last_commit_id(file_path)
        if commit_id:
            file_name, file_extension = os.path.splitext(name)
            new_file_name = f"{file_name}-{commit_id}{file_extension}"
            new_file_path = os.path.join(root, new_file_name)
            
            print(f"Umbenennen: {file_path} zu {new_file_path}")
            os.rename(file_path, new_file_path)
