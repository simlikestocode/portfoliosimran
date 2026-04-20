import os
import shutil

folder_path = input("Enter folder path to organize: ")

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav"]
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        _, extension = os.path.splitext(filename)

        for folder, extensions in file_types.items():
            if extension.lower() in extensions:
                target_folder = os.path.join(folder_path, folder)

                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} → {folder}")
