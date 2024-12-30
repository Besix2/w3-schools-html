import os
import json

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the path to the "ids" folder
IDS_DIR = os.path.join(BASE_DIR, "ids")

# Access the JSON files
free_ids_path = os.path.join(IDS_DIR, "free_ids.json")
occupied_ids_path = os.path.join(IDS_DIR, "occupied_ids.json")

# Example: Load the JSON files
def load_ids(file_name):
    file_path = os.path.join(IDS_DIR, file_name)
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_ids(file_name, content):
    file_path = os.path.join(IDS_DIR, file_name)
    try:
        # Open the file in write mode ('w')
        with open(file_path, 'w') as f:
            # Use json.dump to write the content as JSON
            json.dump(content, f)  # This will serialize the list as JSON and write it to the file
    except FileNotFoundError:
        # Handle the case where the file is not found (it will create the file)
        return []
    

def generate_ids():  # function to generate new ids if the old ones are all occupied
    free_ids = load_ids("free_ids.json")
    occupied_ids = load_ids("occupied_ids.json")
    new_ids = []
    if len(occupied_ids) == 0:
        for i in range(1, 101):
            new_ids.append(i)

    else:
        biggest_id = max(occupied_ids)  # find biggest id to generate new ones starting from there
        biggest_id = biggest_id + 1
        for i in range(biggest_id, biggest_id + 100):  # Generate the next 10 IDs
            new_ids.append(i)
        
    write_ids("free_ids.json", new_ids)

def change_id(id, action): #function to move id from occupied to free and vise versia
    free_ids = load_ids("free_ids.json") 
    occupied_ids = load_ids("occupied_ids.json")
    if action == "occupy":
        occupied_ids.append(id)
        write_ids("occupied_ids.json", occupied_ids)
        free_ids.remove(id)
        write_ids("free_ids.json", free_ids)


def give_smallest_free_id():#function to pick the smallest free id and return it and than put it in occupied
    free_ids = load_ids("free_ids.json")
    if len(free_ids) == 0:
        generate_ids()
        free_ids = load_ids("free_ids.json")
    smallest_free_id = min(free_ids)
    change_id(smallest_free_id, "occupy")
    return smallest_free_id


