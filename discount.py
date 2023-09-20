# Import the datetime class from the datetime module
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
# print(day_of_week)

subtotal = float(input('Please enter the subtotal: '))


if subtotal >= 50:
    if day_of_week == 2 or day_of_week == 3:
        discount = 0.1
        discount_amount = subtotal * discount
        subtotal_after_discount = subtotal - discount_amount
        tax = subtotal_after_discount * 0.06
        total = subtotal_after_discount + tax
        print(f'Discount Amount: {discount_amount:.2f}')
        print(f'Sales tax amount: {tax:.2f}')
        print(f'Total: {total:.2f}')
    else:
        discount = 0
        tax = subtotal * 0.06
        total = subtotal + tax
        print(f'Sales tax amount: {tax:.2f}')
        print(f'Total: {total:.2f}')
else:
    discount = 0
    tax = subtotal * 0.06
    total = subtotal + tax
    print(f'Sales tax amount: {tax:.2f}')
    print(f'Total: {total:.2f}')
