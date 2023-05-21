import os

current_directory = os.getcwd()

files = os.listdir(current_directory)

extensions = set()

# Uzantıları topluyoruz
# Collecting the extensions
for file in files:
    if os.path.isfile(os.path.join(current_directory, file)):
        _, ext = os.path.splitext(file)
        extensions.add(ext)

# Klasörleri oluşturuyoruz
# Creating the folders
for ext in extensions:
    folder_name = ext.strip('.').capitalize()
    folder_path = os.path.join(current_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Dosyaları ilgili klasörlere taşıyoruz
# Moving the files to respective folders
for file in files:
    if os.path.isfile(os.path.join(current_directory, file)):
        _, ext = os.path.splitext(file)
        ext = ext.strip('.')
        folder_name = ext.capitalize()
        file_path = os.path.join(current_directory, file)
        folder_path = os.path.join(current_directory, folder_name)
        new_file_path = os.path.join(folder_path, file)
        os.rename(file_path, new_file_path)

print("Klasörler başarıyla oluşturuldu ve dosyalar taşındı.")
print("Folders created successfully and files moved.")
