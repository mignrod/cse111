"""
This Program creates a list of numbers,
appends more numbers onto the list,
and prints the list.
"""

import random

def main():
    """
    This function starts the program by creating a list named numbers.
    numbers = [16.2, 75.1, 52.3]
    Then, prints the number list and calls the append_random_numbers funtion
    with 1 argument to add 1 number to the list. Prints the list again.
    Finally, calls the append_random_numers again woth 2 arguments to add 3 numbers
    to the list and prints the last list.
    Parameter: None
    """
    numbers_list = [16.2, 75.1, 52.3]
    print(f'numbers {numbers_list}')
    
    append_random_numbers(numbers_list)
    print(f'numbers {numbers_list}')

    append_random_numbers(numbers_list, 3)
    print(f'numbers {numbers_list}')

def append_random_numbers(numbers_list, quantity=1):
    """
    This function computes quantity pseudo random numbers by calling
    the random.uniform function and round the number to one digit after
    the decimal. Then, append the number onto the end of the number list.
    Parameter: A list named numbers_list and a integer named quantity with default value of 1.
    """
    for _ in range(quantity):
        random_numbers = random.uniform(0, 100)
        round_numbers = round(random_numbers, 1)
        numbers_list.append(round_numbers)
    
   

if __name__ == '__main__':
    main()