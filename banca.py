# This program get input from users and save the inputs
# in numerable strings. Compare the results with numbers every hour 
# and mark the correct number until a string achieve 3 consecutive 
# correct numbers. The string that obtins this is winner.

# Import math module and datetime module
import math
from datetime import datetime

# Print a brief explanation to the user
def main():
    time = current_time(datetime)
    prox_sorteo = proximo_sorteo(datetime)
    
    print('Bienvenido a {NOMBRE DEL SORTEO}!!')
    print()
    print('Elige 3 números de tu gusto en el rango del 1 al 38')
    print('Participas durante 12 sorteos consecutivos con los mismos números!')
    print('Mucha Suerte!!')
    print()
    print(f'La hora actual es: {time} y participas desde el sorteo de las {prox_sorteo}')

    # Get inputs form the users.
    # 3 numbers in the range 1-38
    num_1 = int(input('Por favor, ingresa tu primer numero: '))
    num_2 = int(input('Por favor, ingresa tu segundo numero: '))
    num_3 = int(input('Por favor, ingresa tu tercer numero: '))
    print('Por favor, verifica tu jugada!')
    print(f'Los números de tu elección son: {num_1}, {num_2}, y {num_3}')

    check = input('Deseas confirmar (S o N): ')
    user_list = [{num_1}, {num_2}, {num_3}]
    

# Define current time function
def current_time(datetime):
    """Return current hour and minutes.
    Parameter time: as a string in this format: HH-MM
    Return: current hour.
    """
    today = datetime.now()
    hora_m = today.hour
    hora = hora_m -12
    minutos = today.minute
    if hora_m > 12:
        meridian = 'PM'
    else:
        meridian = 'AM'
    time = f'{hora}:{minutos:01} {meridian}'
    return time

# Define what is the next prize
def proximo_sorteo(datetime):
    hora_m = datetime.now().hour
    if hora_m > 12:
        meridian = 'PM'
    else:
        meridian = 'AM'
    prox_sorteo = f'{hora_m - 11}:00 {meridian}'
    return prox_sorteo

main()
