import shutil as sh
import os

# Defining all the extensions i want to organize
extensions = {
    'PDF Files' : ('.pdf'),                                    # PDF extensions
    'Word Files' : ('.doc','.docx','.docm','.dot','.dotx'),    # Word extensions
    'Excel Files' : ('.xls','.xlsx'),                          # Excel extensions    
    'Image Files' : ('.jpg','.jpeg','.png','.gif'),            # Images extensions
    'Powerpoint Files' : ('.ppt','.pptx','.pptm','.xml'),      # Powerpoint extension
    'Book Files' : ('.epub'),                                  # Book extension
    'Zip Files' : ('.zip','.rar'),
    'Software Files' : ('.exe')                               # Program extension
    # 'Others' : None
}


# # Store the parent directory in a variable
parent_dir = r'C:\Users\<username>\Downloads'

# Run a for loop in the dictionary to cycle the keys
for key in extensions.keys():
    new_path = os.path.join(parent_dir,key)     # Join the parent_dir with the keys
    if not os.path.exists(new_path):            # Check if the folder already exists or not
        os.mkdir(new_path)                      # If the path doesn't exists ... create the path (folder)


def file_finder(folder_path,file_extension):
    list_of_files = []
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                list_of_files.append(file)
    return list_of_files

for extension_type, extension_tuple in extensions.items():  # Cycling through dictionary
    folder_path = os.path.join(parent_dir,extension_type)   # Accessing the new folders
    for item in file_finder(parent_dir,extension_tuple):    # Cycling through the files in the parent directory
        item_path = os.path.join(parent_dir,item)           # Accessing the individual file
        sh.move(item_path,folder_path)                      # Moving the file to the folder

