"""
This program can reads the contents of provinces.txt into a list and then modifies the list.
This program do the following:
1. Open the provinces.txt file for reading.
2. Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
3. Print the entire list.
4. Remove the first element from the list.
5. Remove the last element from the list.
6. Replace all occurrences of "AB" in the list with "Alberta".
7. Count the number of elements that are "Alberta" and print that number.
"""

def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    provinces_list = read_list('provinces.txt')

    # Remove first element of the list
    provinces_list.pop(0)

    # Remove last element of the list
    provinces_list.pop()

    # Replace all occurrences of "AB" with "Alberta".
    for i in range(len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = 'Alberta'

    # Print the provinces entire list
    print(provinces_list)

    # Compute the occurrence of the word 'Alberta' by calling the list.count method.
    count = provinces_list.count('Alberta')

    # Print a blank line
    print()

    # Print the occurrence
    print(f'Alberta occurs {count} times in the modified list.')

def read_list(filename):
    """
    Read the content of a text file into a list and return the list.
    Parameter: 'filename' the name of the file to open.
    Returns: a list of string
    """
    # Create an empty list named provinces_list that store the strings.
    provinces_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, 'rt') as provinces_file:

        # Read the contents of the text
        # file one line at a time.
        for line in provinces_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            provinces_list.append(clean_line)
    
    # Return the list of provinces
    return provinces_list

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()