import os
import shutil

print('========== Smart File Organizer Pro ==========')
folder_path= input('''Enter Folder Path:
 
''')
print()

if os.path.isdir(folder_path):
    print(' Folder Found')
    print()
    print('Files Found:')
    print()

    items = os.listdir(folder_path)
    
    FILE_TYPES= { 
    
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",

        ".mp4": "Videos",
        ".mkv": "Videos",

        ".mp3": "Music",

        ".pdf": "Documents",
        ".docx": "Documents",
        ".txt": "Documents", 

        ".py" : "Python"


    }
    for item in items:
        full_path= os.path.join(folder_path , item)


        if os.path.isfile(full_path):
            
            file_name, extension = os.path.splitext(item)
            category = FILE_TYPES.get(extension, 'Others')
            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok = True)
            print(item, '----->', category)
            destination_path= os.path.join(category_folder, item)
            
            if os.path.exists(destination_path):
                counter = 1 
                while True:
                    rec_file = f"{file_name}({counter}){extension}"
                    new_destination_path= os.path.join(category_folder, rec_file)
                    if os.path.exists(new_destination_path):
                        counter+=1
                        

                    else:
                        shutil.move(full_path, new_destination_path)
                        break

            else:
                shutil.move(full_path, destination_path)
                
                
else:
    print(' Invalid Folder Path')












































































































































