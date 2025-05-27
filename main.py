import os
import shutil

allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

source_folder = 'вхідна_текa'
destination_folder = 'зображення'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):
    _, extension = os.path.splitext(filename)
    extension = extension.lower()
    
    if extension in allowed_extensions:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Файл '{filename}' переміщено.")
    else:
        print(f"Пропущено файл: {filename}")
