"""
This program open and read the CSV file named pupils.csv that contains data about 100 students
into a compound list in separate rows. Then the program will sort the list according to differents
arguments, for example, will sorts the list by birthday from oldest to youngest,
and then prints the list with the data about each student on a separate line.
"""

import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    students_list = read_compound_list('pupils.csv')

    sort_birthday = lambda birth: birth[BIRTHDATE_INDEX]
    sort_given_name = lambda given: given[GIVEN_NAME_INDEX]

    def extract_month_day(students_list):
        string = students_list[BIRTHDATE_INDEX]
        month_day = string[5:]
        return month_day
    

    youngest_to_oldest = sorted(students_list, key=sort_birthday)
    given_name = sorted(students_list, key=sort_given_name)
    month_day = sorted(students_list, key=extract_month_day)

    print('Ordered from Oldest to Youngest')
    # print_list(youngest_to_oldest)
    # print_list(given_name)
    print_list(month_day)

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(compound_list):
    """
    This function takes a list as a parameter and prints each element of the list on a separate line.

    Parameter: a list with the content of the CSV file
    Return: The printed list
    """
    for students in compound_list:
        print(students)
    return students

# If this file is executed like this:
# > python pupils.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == '__main__':
    main() 

