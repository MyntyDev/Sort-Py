import os 
import shutil

current_dir = os.getcwd()

folders_created = 0 
files_moved = 0 

for filename in os.listdir(current_dir):

    if not os.path.isfile(os.path.join(current_dir, filename)):
        continue

    # The reason we get the last occurence of the dot is incase the file name is like: filename.file.txt
    last = filename.rindex(".")

    # We add one beacuse we don't want the dot in the folder name (or else the folder becomes hidden)
    extension = filename[last+1:]
    name = filename[:-len(extension)-1]

    organize_folder = f"./{extension}"

    if not os.path.exists(organize_folder):
        os.makedirs(organize_folder)
        folders_created += 1

    shutil.move(f"./{filename}", organize_folder)
    files_moved += 1 


print(f"{files_moved} files moved.")
print(f"{folders_created} folders created.")

