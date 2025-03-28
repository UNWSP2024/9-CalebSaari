# The objective of this task is to create a Python program that reads a series of integers from a
# file named numbers.txt, calculates their total, and appropriately handles any exceptions that may
# arise during the process. The program should be robust enough to manage scenarios such as the
# file not existing, the file being empty, or the presence of non-integer values within the file.

def read_and_sum_numbers(file_path):
    total = 0
    try:
        with open(file_path, 'r') as file:
            numbers = file.readlines()
            if not numbers:
                raise ValueError("The file is empty.")
            for number in numbers:
                try:
                    total += int(number.strip())
                except ValueError:
                    print(f"Warning: '{number.strip()}' is not a valid integer and will be ignored.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return total

if __name__ == "__main__":
    file_path = 'numbers.txt'
    result = read_and_sum_numbers(file_path)
    print(f"The total sum of the integers in the file is: {result}")\

# Caleb Saari 3/27/25 Wk9 Program 3: Average Numbers