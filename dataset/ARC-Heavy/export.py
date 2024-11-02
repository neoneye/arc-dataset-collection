import os
import json
import shutil

def convert_to_arc_format(pair_list, save_filename: str):
    if not isinstance(pair_list, list):
        raise ValueError('pair_list is not a list.')
    train_list = []
    test_list = []
    if len(pair_list) < 10:
        number_of_tests = 1
    elif len(pair_list) < 20:
        number_of_tests = 2
    else:
        number_of_tests = 3
    for pair_index, pair_item in enumerate(pair_list):
        # print(f'Item {pair_index}: {pair_item} {len(pair_item)}')
        if len(pair_item) != 2:
            raise ValueError(f'Item {pair_index} does not have 2 elements.')
        input_image = pair_item[0]
        output_image = pair_item[1]
        dict = {'input': input_image, 'output': output_image}
        if pair_index >= len(pair_list) - number_of_tests:
            test_list.append(dict)
        else:
            train_list.append(dict)
    arc_dict = {'train': train_list, 'test': test_list}
    #print(f'{save_filename}: train {len(train_list)} test {len(test_list)}')
    os.makedirs(os.path.dirname(save_filename), exist_ok=True)
    with open(save_filename, 'w') as f:
        json.dump(arc_dict, f)

def compress_dir(dirname):
    # Compress the directory into a ZIP file
    shutil.make_archive(dirname, 'zip', dirname)
    # Rename the directory by adding 'delete_' prefix
    parent_dir = os.path.dirname(dirname)
    base_dirname = os.path.basename(dirname)
    new_dirname = os.path.join(parent_dir, f'delete_{base_dirname}')
    os.rename(dirname, new_dirname)

dataset_name = 'data_100k'
# dataset_name = 'data_suggestfunction_100k'
file_path = f'{dataset_name}.jsonl'

row_index = -1
with open(file_path, 'r') as f:
    for row_index, line in enumerate(f):
        line = line.strip()
        if not line:
            continue  # Skip empty lines
        data = json.loads(line)

        if row_index % 1000 == 0:
            print(f'Processing row {row_index+1}...')

        if isinstance(data, dict):
            keys = list(data.keys())
            if len(keys) > 1:
                second_key = keys[1]
                dirname = row_index // 1000
                convert_to_arc_format(data[second_key], f'{dataset_name}/{dirname}/{dataset_name}_task{row_index}.json')
                if row_index % 1000 == 999:
                    compress_dir(f'{dataset_name}/{dirname}')
            else:
                print(f'Row {row_index+1} does not have enough columns.')
        else:
            print(f'Row {row_index+1} is not a dict.')

# After the loop, compress the last directory if it hasn't been compressed
if row_index % 1000 != 999:
    compress_dir(f'{dataset_name}/{dirname}')
