import os 
import shutil
import argparse

current_dir = os.getcwd()

def clean_up_extensions(list_of_extensions):
    try:
        return [x.replace(".", "") for x in list_of_extensions]
    except TypeError:
        return None

desc = "Python script to organize files."
parser = argparse.ArgumentParser(description=desc)

# Just incase the user does not want to organize ALL of their files.
parser.add_argument('-f', '--files', nargs="+",  dest='to_exclude', required=False)
parser.add_argument('-x', '--extension', nargs="+", dest="extensions_to_exclude", required=False)

# parse args
args = parser.parse_args()

files_to_exclude = args.to_exclude 
extensions_to_exclude = clean_up_extensions(args.extensions_to_exclude)

folders_created = 0 
files_moved = 0 

for filename in os.listdir(current_dir):

    if not files_to_exclude is None:
        if filename in files_to_exclude:
            continue 

    if not os.path.isfile(os.path.join(current_dir, filename)):
        continue

    # The reason we get the last occurence of the dot is incase the file name is like: filename.file.txt
    last = filename.rindex(".")

    # We add one beacuse we don't want the dot in the folder name (or else the folder becomes hidden)
    
    extension = filename[last+1:]
    name = filename[:-len(extension)-1]

    if not extensions_to_exclude is None:
        # The reason we are replacing every dot with nothing is because our code removes the dots as well
        if extension in extensions_to_exclude:
            continue 

    organize_folder = f"./{extension}"

    if not os.path.exists(organize_folder):
        os.makedirs(organize_folder)
        folders_created += 1

    shutil.move(f"./{filename}", organize_folder)
    files_moved += 1 


print(f"{files_moved} files moved.")
print(f"{folders_created} folders created.")

