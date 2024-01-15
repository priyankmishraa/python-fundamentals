import json

# Script: JSON Module Features in Python

# Explanation: JSON Module Features
# The json module in Python provides features for encoding and decoding JSON data.

# Example 1: Encoding Python Data to JSON
def encode_to_json(data):
    try:
        json_data = json.dumps(data, indent=2)  # Indent for pretty formatting
        return json_data
    except Exception as e:
        return f"Error: {e}"

# Example 2: Decoding JSON Data to Python
def decode_from_json(json_data):
    try:
        python_data = json.loads(json_data)
        return python_data
    except Exception as e:
        return f"Error: {e}"

# Sample data for encoding to JSON
sample_data = {
    "name": "Alice",
    "age": 28,
    "occupation": "Engineer",
    "skills": ["Python", "JavaScript", "Data Analysis"],
}

# Uncomment the lines below to see the behavior of different examples
# json_string = encode_to_json(sample_data)
# decoded_data = decode_from_json(json_string)

# Example 3: Reading and Writing JSON to a File
def read_write_json_file(file_path, data):
    try:
        # Writing JSON to a file
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=2)

        # Reading JSON from a file
        with open(file_path, 'r') as json_file:
            loaded_data = json.load(json_file)

        return loaded_data
    except Exception as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of the JSON file example
# file_data = read_write_json_file("sample.json", sample_data)

