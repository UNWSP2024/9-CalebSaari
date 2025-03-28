# The task is to create a Python program that reads a file named names.txt, which contains a
# series of names, and displays the total number of names stored in that file. This program
# will help in understanding file handling and basic string operations in Python.

def count_names_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            names = file.readlines()
            return len(names)
    except FileNotFoundError:
        return "File not found."

file_path = 'names.txt'
number_of_names = count_names_in_file(file_path)
print(f'Number of names in the file: {number_of_names}')

# Caleb Saari 3/27/25 Wk9 Program 1: Item Counter