import csv

# Script: CSV Module Features in Python

# Explanation: CSV Module Features
# The csv module in Python provides features for reading and writing CSV files.

# Example 1: Writing Data to a CSV File
def write_to_csv(file_path, data):
    try:
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Name', 'Age', 'Occupation'])  # Writing header
            for person in data:
                csv_writer.writerow(person)
        return f"CSV file created at {file_path}"
    except Exception as e:
        return f"Error: {e}"

# Example 2: Reading Data from a CSV File
def read_from_csv(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  # Reading the header
            data = [row for row in csv_reader]
        return header, data
    except Exception as e:
        return f"Error: {e}"

# Sample data for writing to a CSV file
sample_data = [
    ['Alice', 28, 'Engineer'],
    ['Bob', 35, 'Teacher'],
    ['Charlie', 42, 'Doctor'],
]

# Uncomment the lines below to see the behavior of different examples
# result1 = write_to_csv("sample.csv", sample_data)
# header, data = read_from_csv("sample.csv")

# Example 3: Reading and Writing CSV Files with DictReader and DictWriter
def read_write_dict_csv(file_path):
    try:
        with open(file_path, 'w', newline='') as csv_file:
            fieldnames = ['Name', 'Age', 'Occupation']
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()  # Writing header
            for person in sample_data:
                csv_writer.writerow({'Name': person[0], 'Age': person[1], 'Occupation': person[2]})

        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            header = csv_reader.fieldnames
            data = [row for row in csv_reader]
        return header, data
    except Exception as e:
        return f"Error: {e}"

# Uncomment the lines below to see the behavior of the DictReader and DictWriter example
# header_dict, data_dict = read_write_dict_csv("dict_sample.csv")


# --------------------
# OUTPUT
# --------------------

# CSV file created at sample.csv
