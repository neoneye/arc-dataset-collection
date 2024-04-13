from main import *
import os
import json

def arc_dict_from_flat_array(tasks):
    """
    Given a flat array of tasks, returns a dictionary formatted for the ARC,
    with the first N-1 tasks in 'train' and the last task in 'test'.
    """
    if len(tasks) > 1:
        return {'train': tasks[:-1], 'test': [tasks[-1]]}
    return None  # Return None if not enough tasks to split

def export_easy_hard_from_dataset(
    folder: str = 're_arc',
    n: int = 8,
    s: int = 0,
    e: int = 400
) -> None:
    """
    export json files with ARC file format from a generated dataset
    """
    # Create directories if they don't exist
    easy_dir = f'{folder}/easy'
    hard_dir = f'{folder}/hard'
    os.makedirs(easy_dir, exist_ok=True)
    os.makedirs(hard_dir, exist_ok=True)

    with open(f'{folder}/metadata.json', 'r') as fp:
        metadata = json.load(fp)
    for i, fn in enumerate(sorted(os.listdir(f'{folder}/tasks'))):
        if s <= i < e:
            key = fn[:8]
            with open(f'{folder}/tasks/{key}.json', 'r') as fp:
                generated_task = json.load(fp)
            generated_task = [format_example(example) for example in generated_task[:10*n]]
            difficulties = metadata[key]['pso_difficulties'][:9*n]
            generated_task = [ex for ex, diff in sorted(zip(generated_task, difficulties), key=lambda item: item[1])]
            easy = generated_task[1*n:2*n]
            hard = generated_task[8*n:9*n]

             # Save tasks to respective directories
            easy_root_dict = arc_dict_from_flat_array(easy)
            hard_root_dict = arc_dict_from_flat_array(hard)

            if easy_root_dict:
                with open(f'{easy_dir}/{key}.json', 'w') as ef:
                    json.dump(easy_root_dict, ef)
            if hard_root_dict:
                with open(f'{hard_dir}/{key}.json', 'w') as hf:
                    json.dump(hard_root_dict, hf)

export_easy_hard_from_dataset()
