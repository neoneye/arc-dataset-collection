import os
import shutil

# Define the source directory where the nested directories are located
source_dir = 'input'
# Define the target directory where the files will be moved to
target_dir = 'output_a'

# Ensure the target directory exists
os.makedirs(target_dir, exist_ok=True)

# Iterate over each directory and subdirectory in the source directory
for dirpath, dirnames, filenames in os.walk(source_dir):
    # Extract the directory name
    dir_name = os.path.basename(dirpath)
    
    for filename in filenames:
        # Check if the file is a JSON file and does not end with '_soln.json'
        if filename.endswith('.json') and not filename.endswith('_soln.json'):
            # Construct the new filename
            new_filename = f"{dir_name}_{filename}"
            # Define the full path of the source file
            source_file = os.path.join(dirpath, filename)
            # Define the full path for the new file in the target directory
            target_file = os.path.join(target_dir, new_filename)
            
            # Move and rename the file to the target directory
            shutil.move(source_file, target_file)

print("Files have been moved and renamed.")
