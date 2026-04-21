import os

folders = ['images', 'output', 'data', 'scripts']
for folder in folders:
    os.makedirs(folder, exist_ok=True)