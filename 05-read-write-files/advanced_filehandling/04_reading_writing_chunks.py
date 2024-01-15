# Script: Reading and Writing in Chunks in Python

# Explanation: Reading and Writing in Chunks
# Reading and writing files in chunks is useful for efficiently handling large files.

# Example 1: Reading a File in Chunks
def read_file_in_chunks(file_path, chunk_size=1024):
    try:
        with open(file_path, 'r') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                process_chunk(chunk)
    except FileNotFoundError as e:
        return f"Error: {e}"

def process_chunk(chunk):
    # Placeholder for processing logic
    print(f"Processing Chunk: {chunk}")

# Uncomment the line below to see the behavior of reading a file in chunks
# read_file_in_chunks("large_file.txt")

# Example 2: Writing to a File in Chunks
def write_to_file_in_chunks(file_path, data, chunk_size=1024):
    try:
        with open(file_path, 'w') as file:
            for i in range(0, len(data), chunk_size):
                chunk = data[i:i + chunk_size]
                file.write(chunk)
    except Exception as e:
        return f"Error: {e}"

# Uncomment the line below to see the behavior of writing to a file in chunks
# write_result_in_chunks = write_to_file_in_chunks("output_file.txt", "Lorem ipsum dolor sit amet, consectetur adipiscing elit." * 1000)

# Example 3: Reading Binary File in Chunks
def read_binary_file_in_chunks(file_path, chunk_size=1024):
    try:
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                process_binary_chunk(chunk)
    except FileNotFoundError as e:
        return f"Error: {e}"

def process_binary_chunk(chunk):
    # Placeholder for processing binary chunk logic
    print(f"Processing Binary Chunk: {chunk}")

# Uncomment the line below to see the behavior of reading a binary file in chunks
# read_binary_file_in_chunks("binary_file.bin")

# -----------------------
# OUTPUT
# -----------------------

# Processing Chunk: Lorem ipsum dolor sit amet, consectetur adipiscing elit....
