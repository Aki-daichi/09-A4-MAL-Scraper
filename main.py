import json

file_location = 'manga\hasil.json'
# Load the JSON data
with open(file_location, 'r', encoding='utf-8', errors='ignore') as file:
    data = json.load(file)

# Define the sorting key function
def get_sorting_key(item):
    return int(item['rank'])

# Sort the data based on the 'rank' value
sorted_data = sorted(data, key=get_sorting_key)

# Save the sorted data back to a JSON file
with open(file_location, 'w') as file:
    json.dump(sorted_data, file, indent=4)