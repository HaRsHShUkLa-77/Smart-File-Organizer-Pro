import os
import shutil
import logging
logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO
)

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

    total_files = 0
    success_files = 0
    failed_files = 0
    for item in items:

        full_path= os.path.join(folder_path , item)
          

        if os.path.isfile(full_path):
            total_files += 1
            
            file_name, extension = os.path.splitext(item)
            category = FILE_TYPES.get(extension, 'Others')
            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok = True)
            print(item, '----->', category)
            destination_path= os.path.join(category_folder, item)
            
            if os.path.exists(destination_path):
                counter=1
                while True:

                    rec_file = f"{file_name} ({counter}){extension}"
                    new_destination_path= os.path.join(category_folder, rec_file)
                    if os.path.exists(new_destination_path):
                        counter+=1
                    else:
                        final_destination = new_destination_path
                        break
            

            else:
                final_destination = destination_path

            
            file = os.path.basename(final_destination)
            

            try:
                shutil.move(full_path, final_destination)
                success_files +=1
                print(f"Success: Moved '{full_path}' to '{final_destination}'")
                logging.info(f"Success: Moved '{full_path}' to '{final_destination}'")
            except FileNotFoundError:
                failed_files +=1
                print(f"Error: Source file ya path '{full_path}' nahi mila.")
            except PermissionError:
                print(f"Error: Permission denied! File move karne ka access nahi hai.")
            except shutil.Error as e:
                print(f"Shutil Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
            
    print("\n========== Summary ==========")
    print(f"Total Files          : {total_files}")
    print(f"Moved Successfully   : {success_files}")
    print(f"Failed               : {failed_files}")
    print("============================")

            
               
else:
    print(' Invalid Folder Path')















































































