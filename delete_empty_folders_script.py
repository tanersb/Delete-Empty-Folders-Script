import os
import shutil

def delete_empty_folders(folder_path):
    contents = os.listdir(folder_path)
    
    for item in contents:
        item_path = os.path.join(folder_path, item)
        
        # Eğer bir klasörse ve içi boşsa, sil
        if os.path.isdir(item_path):
            if not os.listdir(item_path):
                print("Deleting empty folder:", item_path)
                shutil.rmtree(item_path)
            else:
                # Klasör doluysa, içeriğini kontrol et
                delete_empty_folders(item_path)

current_directory = os.getcwd()

delete_empty_folders(current_directory)
