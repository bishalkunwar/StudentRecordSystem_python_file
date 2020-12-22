#Python code to implement file handling and to perform crud operations and methods. // Record System reference student record system
#Learning objectives:
'''1:File Handling
2: crud operations
3: Class object and getter setter
4: exceptions
5: methods
6: ELIF'''
#Solution:

import pickle

# here i am going to create the Record system using class and object
class passenger:
    # The _ _init_ _ method to initialize the attributes.
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    # The set_name method sets the name attribute.
    def set_name(self, name):
        self.__name = name

    # The set_phone method sets the phone attribute.
    def set_phone(self, phone):
        self.__phone = phone

    # The set_email method sets the email attribute.
    def set_email(self, email):
        self.__email = email

    # The get_name method returns the name attribute.
    def get_name(self):
        return self.__name

    # The get_phone method returns the phone attribute.
    def get_phone(self):
        return self.__phone

    # The get_email method returns the email attribute.
    def get_email(self):
        return self.__email

    # The _ _str_ _ method returns the object's state
    # as a string.
    def __str__(self):
        return "Name: " + self.__name + \
               "\nPhone: " + self.__phone + \
               "\nEmail: " + self.__email


# define global constants for main menu choices
create_ticket = 1
search_ticket = 2
edit_ticket = 3
delete_ticket = 4
exit_system = 5

FILENAME = 'records.dat'

import sys
import pickle


def main():
    choice = 0
    while choice != exit_system:
        choice = menu_board()

        if choice == create_ticket:
            add()
        elif choice == search_ticket:
            search()
        elif choice == edit_ticket:
            edit()
        elif choice == delete_ticket:
            delete()
        elif choice == exit_system:
            sys.exit()
        else:
            print("invalid choice:")


def menu_board():
    print()
    print('Menu')
    print('---------------------------')
    print('1: add ticket')
    print('2: search ticket')
    print('3: edit ticket')
    print('4: Delete  ticket')
    print('5: Quit the program')
    print()
    # Get the user's choice.
    choice = int(input('Enter your choice: '))
    # Validate the choice.
    while choice < create_ticket or choice > exit_system:
        choice = int(input('Enter a valid choice: '))
    # return the user's choice.
    return choice


def load_tickets():
    try:
        # Open the tickets.dat file.
        input_file = open(FILENAME, 'rb')
        # Unpickle the dictionary.
        tickets_dct = pickle.load(input_file)
        # Close the ticket_inventory.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        tickets_dct = {}
        # Return the dictionary.
    return tickets_dct


def add():
    # Get the ticket info and passenger info.
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')
    # Create a passenger object named entry.
    # sir, i got stuck here in ticketd.passenger
    entry = passenger(name, phone, email)
    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.

    if phone or email not in passenger:
        #  passenger[name] = entry
        save_tickets(entry)  # save ticket
        print('The ticket has been added.')
    else:
        print('That name already exists.')


def search():
    # Get a name to look up.
    name = input('Enter a name: ')
    # Look it up in the dictionary.
    try:
        pickle_in = open(name + ".txt", "rb")
        search_value = pickle.load(pickle_in)
        flag = search_value.get_name()  # searching name in dictionary
        print("Name found: " + flag)
    except:
        print('Not found')


def edit(passenger):
    # Get a name to look up.
    name = input('Enter the name: ')

    if name in passenger:
        name = input('name:')
        # Get a new phone number.
        phone = input('number: ')
        # Get a new email address.
        email = input('email address: ')
        # Create a contact object named entry.
        entry = passenger(name, phone, email)
        # Update the entry.
        passenger[name] = entry
        print('ticket has been updated.')
    else:
        print('That name is not found.')


def delete(passenger):
    # Get a name to look up.
    name = input('name: ')
    # If the name is found, delete the entry.
    if name in passenger:
        del passenger[name]
        print('ticket deleted.')
    else:
        print('That name is not found.')


def save_tickets(entry):
    # Open the file for writing.1
    file_name = entry.get_name()
    output_file = open(file_name + ".txt", 'wb')
    # Pickle the dictionary and save it.1

    pickle.dump(entry, output_file)
    # Close the file.
    output_file.close()
    # Call the main function.


main()