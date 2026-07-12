import os

print('========== Smart File Organizer Pro ==========')
folder_path= input('''Enter Folder Path:
 
''')
print()

if os.path.isdir(folder_path):
    print('✔ Folder Found')
    print()
    print(folder_path)
    print()
    items = os.listdir(folder_path)
    for item in items:
        print(item)
else:
    print('❌ Invalid Folder Path')


