import os
import shutil

def copy_and_rename_files(source_folder, destination_folder):
    
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

   
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        
        if filename == '.nomedia' or not os.path.isfile(source_path):
            continue
 
        new_filename = f"STIMG_{filename}"
        destination_path = os.path.join(destination_folder, new_filename)

        
        shutil.copy2(source_path, destination_path)
        print(f"Copied and renamed {filename} to {new_filename}")



source_folders = ['/storage/emulated/0/WhatsApp/Media/.Statuses', '/storage/emulated/0/WhatsApp Business/Media/.Statuses']
destination_folder = '/storage/emulated/0/Statuses'

for i in source_folders:
    copy_and_rename_files(i, destination_folder)

