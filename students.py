import csv
"""
This program examine the students.csv file and search the user input 
to find the student in the dictionary.
"""

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    students = read_dictionary('students.csv', I_NUMBER_INDEX)
    key_student = input('Please enter an I-Number (xx-xxx-xxxx): ')

    # Remove the dashes from the user input
    key_student = key_student.replace('-', '')

    # 
    if not key_student.isdigit():
        print('Invalid character in I-Number')
    else:
        if len(key_student) < 9:
            print('Invalid I-Number: too few digits')
        elif len(key_student) > 9:
            print('Invalid I-Number: too many digits')
        else:
            if key_student in students:
                value = students[key_student]
                name = value[NAME_INDEX]
                print(name)
            else:
                print('No such student')




def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Create an empty dictionary that store the student data
    students = {}

    # Open the text file for reading and store a reference
    # to the opened file in a variable named student.
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)

        # Skip the firts line
        next(reader)

        # Add every row line into the students dictionary 
        for row_list in reader:
            key = row_list[key_column_index]
            students[key] = row_list

    return students

# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()