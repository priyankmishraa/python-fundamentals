# Script: Reading and Writing Binary Files in Python

# Explanation: Reading and Writing Binary Files
# Binary files in Python can be read and written using the 'rb' and 'wb' modes, respectively.

# Example 1: Reading a Binary File
def read_binary_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of reading a binary file
# binary_content = read_binary_file("binary_file.bin")

# Example 2: Writing to a Binary File
def write_to_binary_file(file_path, data):
    try:
        with open(file_path, 'wb') as file:
            file.write(data)
        return f"Data written to {file_path}"
    except Exception as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of writing to a binary file
# write_result_binary = write_to_binary_file("output_binary_file.bin", b'Binary data example.')

# Example 3: Reading and Writing Binary Files in Chunks
def read_write_binary_file_in_chunks(input_path, output_path, chunk_size=1024):
    try:
        with open(input_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
            while True:
                chunk = input_file.read(chunk_size)
                if not chunk:
                    break
                output_file.write(chunk)
        return f"Binary file copied from {input_path} to {output_path}"
    except FileNotFoundError as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of reading and writing binary files in chunks
# copy_result = read_write_binary_file_in_chunks("binary_file_to_copy.bin", "copied_binary_file.bin")
