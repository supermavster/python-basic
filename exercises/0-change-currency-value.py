# -*- codign: utf-8 -*-
import sys
import os

# Variables & Const
global currencies
global options

currencies = {
    'USD_COP': 3693.94,
    'COP_MXN': 6.02,
    'cop': 'Pesos Colombianos',
    'usd': 'Dollares Americanos',
    'mxn': 'Pesos Mexicanos'
}

options = [
    'COP to USD',
    'COP to MXN',
    'USD to COP',
    'MXN to COP',
    'Exit'
]


def run():
    show_title()
    read_element()


def read_element():
    """Execute and make the process of the actions specifics"""
    option = 0
    while option != len(options) - 1:
        show_menu()
        input_data = _get_client_field('Options: ')
        if not __empty(input_data) and (input_data.isdigit() == True):
            option = int(input_data)
            switch(option)


def show_title():
    """Show custom title of 'Platzi Currency exchange'"""
    complement = (
        '\n                                                                __                          ')
    title = ('\n  _______  _______________  ____  _______  __   ___  _  _______/ /_  ____ _____  ____ ____  ')
    title += ('\n / ___/ / / / ___/ ___/ _ \/ __ \/ ___/ / / /  / _ \| |/_/ ___/ __ \/ __ `/ __ \/ __ `/ _ \ ')
    title += ('\n/ /__/ /_/ / /  / /  /  __/ / / / /__/ /_/ /  /  __/>  </ /__/ / / / /_/ / / / / /_/ /  __/ ')
    title += ('\n\___/\__,_/_/  /_/   \___/_/ /_/\___/\__, /   \___/_/|_|\___/_/ /_/\__,_/_/ /_/\__, /\___/  ')
    title += ('\n                                    /____/                                    /____/        ')
    # Add Styles
    break_line = ('-' * len(complement) + "\n") * 2
    print("{}\n{}\n{}\n".format(break_line, title, break_line))


def show_menu():
    """Show the menu of 'Platzi Seller'"""
    print("Write a number of the next options:")
    for key, value in enumerate(options):
        print("{}. {}".format(key, value))


def switch(option):
    if option == 0:
        currencyExchange('cop', 'usd')
    elif option == 1:
        currencyExchange('cop', 'mxn')
    elif option == 2:
        currencyExchange('usd', 'cop')
    elif option == 3:
        currencyExchange('mxn', 'cop')
    elif option == (len(options) - 1):
        exit_software()
    else:
        print('Invalid Option')
        exit_software()


def currencyExchange(main, secondary):
    print(
        f'Dite la cantidad de {currencies.get(main)} a {currencies.get(secondary)} que desea saber')
    value = float(_get_client_field('value:\t'))
    complement = main.upper() + '_' + secondary.upper()
    complement_tmp = secondary.upper() + '_' + main.upper()
    print("=*" * 30)
    print(
        f'El resultado de {currencies.get(main)} a {currencies.get(secondary)} es: ')
    if complement in currencies.keys():
        print(f'${value * currencies.get(complement)}')
    elif complement_tmp in currencies.keys():
        print(f'${value / currencies.get(complement_tmp)}')
    else:
        print('No Exist Currency')
    print("=*" * 30)
    print('\n\n')

def exit_software():
    sys.exit(0)
    return "Good Bye!"


# Complements
def __empty(value):
    response = True
    if value and value != None:
        if len(value) >= 0:
            response = False
    return response


def _get_client_field(message):
    field = None
    while __empty(field):
        field = input(f'\n{message}')
    return field


if __name__ == "__main__":
    run()
