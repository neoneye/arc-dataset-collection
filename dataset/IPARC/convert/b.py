import json
import os

def convert_json_file(original_file_path, new_file_path):
    # Load the original JSON file
    with open(original_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Split the data
    if len(data) > 1:
        train_data = data[:-1]
        test_data = [data[-1]]
    else:
        # Handle case where there's only one item in the array
        train_data = []
        test_data = data
    
    # Prepare the new structure
    new_data = {
        "train": train_data,
        "test": test_data
    }
    
    # Write the new JSON file
    with open(new_file_path, 'w', encoding='utf-8') as file:
        json.dump(new_data, file, ensure_ascii=False, indent=4)

def convert_all_json_files_in_directory(directory_path, output_directory_path):
    # Ensure output directory exists
    if not os.path.exists(output_directory_path):
        os.makedirs(output_directory_path)

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            original_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(output_directory_path, filename)
            convert_json_file(original_file_path, new_file_path)
            print(f"Converted {filename}")

# Example usage
directory_path = 'output_a'
output_directory_path = 'output_b'
convert_all_json_files_in_directory(directory_path, output_directory_path)
