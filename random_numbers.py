"""
This Program creates a list of numbers,
appends more numbers onto the list,
and prints the list.
"""

import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(f'numbers {numbers}')

    append_random_numbers(numbers)
    print(f'numbers {numbers}')

    append_random_numbers(numbers, 3)
    print(f'numbers {numbers}')

    words_list = []
    append_random_words(words_list, 5)
    print(f'words {words_list}')

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        number = round(random.uniform(0, 100), 1)
        numbers_list.append(number)
    
def append_random_words(words_list, quantity=1):
    words = ['love', 'war', 'smile', 'head', 'arms', 'eyes']
    for _ in range(quantity):
        word = random.choice(words)
        words_list.append(word)


if __name__ == '__main__':
    main()