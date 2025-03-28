# The objective of this task is to develop a Python program that generates a specified number of
# random integers, each ranging from 1 to 500, and writes these integers to a file. The user will
# be prompted to input the desired quantity of random numbers, with a maximum limit of 1000.

import random

def generate_random_numbers(file_name, count):
    if count < 1 or count > 1000:
        raise ValueError("Count must be between 1 and 1000.")

    random_numbers = [random.randint(1, 500) for _ in range(count)]

    with open(file_name, 'w') as file:
        for number in random_numbers:
            file.write(f"{number}\n")

    print(f"{count} random numbers have been written to {file_name}.")

def main():
    file_name = input("Enter the name of the file to save random numbers (e.g., random_numbers.txt): ")
    count = int(input("How many random numbers would you like to generate (1-1000)? "))

    try:
        generate_random_numbers(file_name, count)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

# Caleb Saari 3/27/25 Wk9 Program 2: Random Number File Writer