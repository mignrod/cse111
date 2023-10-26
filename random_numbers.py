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
    numbers = [16.2, 75.1, 52.3]
    print(f'numbers {numbers}')

    # Call the append_random_numbers funtion to
    # add one random number to the numbers list.
    append_random_numbers(numbers)
    print(f'numbers {numbers}')

    # Call the append_random_numbers funtion to
    # add three random numbers to the numbers list.
    append_random_numbers(numbers, 3)
    print(f'numbers {numbers}')

    # Create a list to store rrndom words.
    words_list = []

    # Call de append_random_words function
    # to add one random word to the list.
    append_random_words(words_list)
    print(f'words {words_list}')
    
    # Call de append_random_words function
    # to add five random words to the list.
    append_random_words(words_list, 5)
    print(f'words {words_list}')

def append_random_numbers(numbers_list, quantity=1):
    """
    This function computes quantity pseudo random numbers by calling
    the random.uniform function and round the number to one digit after
    the decimal. Then, append the number onto the end of the number list.
    Parameter: A list named numbers_list and a integer named quantity with default value of 1.
    return: nothing
    """
    for _ in range(quantity):
        number = round(random.uniform(0, 100), 1)
        numbers_list.append(number)
    
def append_random_words(words_list, quantity=1):
    """
    This function computes quantity pseudo random numbers by calling
    the random.uniform function and round the number to one digit after
    the decimal. Then, append the number onto the end of the number list.
    Parameter: A list named numbers_list and a integer named quantity with default value of 1.
    return: nothing
    """

    # Create a list of words to randomly choose from.
    words = ['hearth', 'love', 'join', 'war', 'head', 'hands',\
            'eyes', 'body', 'clouds', 'heaven', 'ground',\
            'smile', 'laugh', 'scream', 'work', 'travel']
    
    # Randomly choose a quantity of words and appen them onto words_list.
    for _ in range(quantity):
        word = random.choice(words)
        words_list.append(word)


if __name__ == '__main__':
    main()