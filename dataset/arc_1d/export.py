import os
import json

tasks_dir = "tasks"
output_dir = "combined_tasks"
batch_size = 8          # how many JSON files go into one combined file
max_combined_files = 10 # max number of combined files per subdir

# Create main output folder if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# We'll keep track of how many combined files we've created per subdir
subdir_counters = {}

for root, dirs, files in os.walk(tasks_dir):
    # Identify JSON files
    json_files = [f for f in files if f.endswith(".json")]
    if not json_files:
        continue  # Skip if no JSON files

    # Sort or shuffle as needed
    json_files = sorted(json_files)

    # Subdirectory name
    subdir_name = os.path.basename(root)

    # Create subdirectory under output_dir if it doesn’t already exist
    subdir_outpath = os.path.join(output_dir, subdir_name)
    if not os.path.exists(subdir_outpath):
        os.makedirs(subdir_outpath)

    # Initialize the counter if not present
    if subdir_name not in subdir_counters:
        subdir_counters[subdir_name] = 0

    # Group files in batches of batch_size
    for start_idx in range(0, len(json_files), batch_size):
        # If we’ve reached or exceeded the maximum allowed combined files,
        # skip remaining batches for this subdir.
        if subdir_counters[subdir_name] >= max_combined_files:
            break

        batch_files = json_files[start_idx : start_idx + batch_size]
        if len(batch_files) < batch_size:
            # Not enough to form a full group -> skip or handle differently
            continue

        # Collect tasks from these JSON files
        all_tasks = []
        for f in batch_files:
            file_path = os.path.join(root, f)
            with open(file_path, "r") as rf:
                data = json.load(rf)
            # Assume there's at least one puzzle in "test"
            if "test" in data and data["test"]:
                all_tasks.append(data["test"][0])

        # If we have exactly batch_size tasks, combine them:
        # (batch_size - 1) tasks go into "train", 1 task goes into "test"
        if len(all_tasks) == batch_size:
            combined_data = {
                "train": all_tasks[: batch_size - 1],
                "test": [all_tasks[batch_size - 1]],
            }

            # Use the current index for the subdir
            current_index = subdir_counters[subdir_name]
            combined_filename = f"{subdir_name}_{current_index}.json"
            combined_path = os.path.join(subdir_outpath, combined_filename)

            # Write the combined JSON
            with open(combined_path, "w") as wf:
                json.dump(combined_data, wf, indent=2)

            print(f"Created: {combined_path}")

            # Increment counter for the subdir
            subdir_counters[subdir_name] += 1
