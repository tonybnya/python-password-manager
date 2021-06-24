'''
PYTHON PASSWORD MANAGER.

A mini program to manage passwords.
Generate a password for a given account.
Store data into a database text file.

Tasks:
    - Create a database file to store all the generated passwords.
    - Create a basic and neatly CLI.

Requirements:
    - User can generate a password.
    - User can store a password into a json database file.
    - User can get a stored password, automatically copied to the clipboard.
    - User can print a view of the json database file.
    - User can delete a stored password.
'''

import clipboard
import json
import os
import random
import re
import string
import sys
import time


# Generate a password, by combining numbers, letters (upper & lower) and symbols.
def generate(length):
    '''
    Takes an integer as the length of the password to generate.
    Arg:
        length (int): length of the password.
    Returns:
        pwd (str): a random string with the given length.
    '''

    # Define a variable to store all letters in lowercase.
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    # Define a variable to store all uppercases.
    uppers = lowers.upper()
    # Define a variable to store a string with all digits.
    numbers = '0123456789'
    # 'string.punctuation' generate all the symbols.
    # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    symbols = string.punctuation
    # Merge all these variables into one.
    merge = lowers + uppers + numbers + symbols
    # Generate a random password, with a given length.
    pwd = ''.join(random.sample(merge, length))

    return pwd

# Define a function to check if the file exists.
def found(filename):
    '''
    Takes a file to check if it exists yet.
    Arg:
        filename (file): filename to check.
    Returns:
        f (bool): a boolean to confirm if the file already exists or not yet.
    '''

    # Check if the database file exists.
    f = os.path.exists(filename)    # True or False.
    if f == True:
        return f
    else:
        return f

# Define a function to add a generated password and the given account to a file.
def add(filename):
    '''
    Takes a file to append data to it.
    Arg:
        filename (file): filename to handle.
    Returns:
        None
        Just print out data added to the file.
    '''

    # String of characters to build a neatly heading.
    line = '+' + '-'*31 + '+'
    # Ask from the user an account to generate its password.
    account = input('Account: ')
    # Ask from the user to give a desired length of the password.
    length = input('Length of the password: ')
    # Check if the given length is a digit.
    if length.isdigit():
        # Transform the given length into an integer.
        length = int(length)
        # Define a loop to check the conformity of the given length.
        # A secure password must contain at least 8 characters, so check it.
        while length < 8:
            print('A password must contain at least 8 characters.')
            account = input('Account: ')
            length = input('Length of the password: ')
            if length.isdigit():
                length = int(length)
            # If the given lenght is correct, assign it to a variable.
            if length >= 8:
                break
    # If the given length is no a digit, print a message to the user.
    else:
        print('Type in an integer next time.')
        sys.exit(1)
    # Define a loop to generate and validate the generated password.
    while True:
        # Call generate function with the right length of the password.
        g = generate(length)
        time.sleep(0.1)
        print(g)
        # Ask the user if the generated password is satisfied.
        answer = input('Password satisfied (y/n)?: ').lower()
        # If the answer is yes, write account and password to the file.
        if answer == 'y':
            # Open the database file into the append mode.
            # Use `try` and `except` block to handle exceptions.
            try:
                with open(filename, 'a') as f:
                    f.write(f'{account.title()}: {g}\n')
                # Print out data stored into the file.
                print()
                # The given account will be stored and formatted with title().
                print(f'{account.title()}: Password: {g}')
                print('Added to the database file!')
                print(line)
                # Break the loop.
                break
            except FileNotFoundError:
                print(f'Could not open `{filename}`.')
        # If the answer is no, continue looping.
        elif answer == 'n':
            continue
        else:
            # If the answer isn't valid, break the loop.
            print('Invalid answer.')
            break

# Define a function to get a stored password.
def get_pwd(filename, account):
    '''
    Takes the database file to handle.
    Args:
        filename (file): a text file.
        account (txt): a string as a given account to get its password.
    Returns:
        passwords (dict): a dictionary with the given account and its password.
    '''

    # Define an empty dictionary.
    passwords = {}
    # Use `try` and `except` block to handle exceptions.
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                if account in line:
                    data = line.rstrip()
                    account, pwd = data.split(': ')
                    passwords[account] = pwd
                else:
                    return f'{account} does not exist.'
    except FileNotFoundError:
        print(f'Could not read `{filename}`.')
    else:
        # Return dictionary filled by data.
        return passwords

# Define a function to delete a stored password.
def delete(filename, account):
    '''
    Takes the database file to delete data into it.
    Args:
        filename (file): file to handle.
        account (txt): a string as given accout to delete with its password.
    Returns:
        - When the file exists, data to delete.
        - When the file does not exist, a string to say it.
    '''

    account = input('Account to delete\n: ').title()
    # Define an empty dictionary.
    my_dict = {}
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                match = re.search(pattern, line)
        # If there is a match, perform some tasks.
        if match:
            data = match.group().rstrip()
            account, pwd = data.split(': ')
            # Store matching data into the defined dictionary.
            my_dict[account] = pwd
            result = json.loads(my_dict)
            return result
        else:
            # If there is no a match, print out a message for that.
            return f'Account `{account}` does not exist yet!'

        with open(filename, 'w') as f:
            data = f.readlines()
            for line in data:
                if line.strip('\n') != match:
                    f.write(line)
    except FileNotFoundError:
        pass
        #print(f'Could not open `{filename}`.')

# Define a function to view the content of the database file.
def view(filename):
    '''
    Takes the database file to print out the content.
    Arg:
        filename (file): file to print out the content.
    Returns:
        passwords (dict): a dictionary with accounts and corresponding passwords.
    '''

    # Define an empty dictionary.
    passwords = {}
    # Open the database file into the read mode.
    try:
        with open(filename, 'r') as f:
            # Define a loop to browse all the lines into the database file.
            for line in f.readlines():
                # 'rstrip()' is to remove all the default \n on each line.
                data = line.rstrip()
                # split : and spaces for each line.
                # Returns a list of 2 items, account & password on each line.
                account, pwd = data.split(': ')
                # Store each account as key with its password as value
                # into the empty dictionary defined above.
                passwords[account] = pwd
    except FileNotFoundError:
        print(f'Could not read `{filename}`.')
    else:
        return passwords

# Define a function with a neatly CLI and the main loop.
def main():
    # Create 'text_files/' in the current folder.

    # file1, the relative path (filename) to the database text file.
    file1 = 'text_files/passwords.txt'
    # file2, the relative path (filename) to the manual text file.
    file2 = 'text_files/manual.txt'

    # Create the database file 'passwords.txt' into it.
    file1 = 'text_files/passwords.txt'
    # Create the manual text file 'manual.txt' into it.
    file2 = 'text_files/manual.txt'

    line = '+' + '-'*31 + '+'
    heading = '|           + MENU +            |'
    if len(sys.argv) == 1:
        print(line)
        print(heading)
        print(line)
        print('|  1. Add a new password        |')
        print('|  2. Get a password            |')
        print('|  3. Delete a password         |')
        print('|  4. View all the passwords    |')
        print('|  Q. Quit                      |')
        print(line)
        # Main loop for the program.
        while True:
            choice = input(': ')

            # If conditions for the menu above.
            if choice == 'q' or choice == 'Q':
                print('Exit...')
                time.sleep(0.1)
                break

            if choice == '1':
                # Call the add function.
                add(file1)

            elif choice == '2':
                # First check if the file exists.
                f = found(file1)
                if f == True:
                    # Call the get_pwd function and assign the return value.
                    result = get_pwd(file1)
                    # Ask the user to type in an account.
                    account = input('Account to get its password\n: ').title()
                    if account in result.keys():
                        pwd = result[account]
                        # Copy the corresponding password to the clipboard.
                        text = clipboard.copy(pwd)
                        print(line)
                        print('|           + VIEW +            |')
                        print(line)
                        print(f' Account `{account}` found.')
                        print(f' Password `{pwd}` copied to clipboard.')
                        print(line)
                    else:
                        print(line)
                        print('|           + VIEW +            |')
                        print(line)
                        print(f' -> Account `{account}` not found.')
                        print(line)
                else:
                    print(f'The database file does not exist.')

            elif choice == '3':
                # First check if the file exists.
                f = found(file1)
                if f == True:
                    # Call the delete function.
                    result = delete(file1)
                    account, pwd = result.keys(), result.values()
                    try:
                        with open(file1) as f:
                            first_char = f.read(1)
                            if not first_char:
                                print(f'`{file1}` is empty.')
                            else:
                                result = delete(file1)
                    except FileNotFoundError:
                        print(f'Could not open `{file1}`.')
                    else:
                        print(f'Data to delete: `{account} : {pwd}`')
                        print('...')
                        time.sleep(0.1)
                        print(f'Account `{account}` successfully deleted.\n')
                else:
                    print(f'The database file does not exist.')

            elif choice == '4':
                # First check if the file exists.
                f = found(file1)
                if f == True:
                    # Call the view password and assign the return value.
                    pwd = view(file1)
                    print(line)
                    print('|           + VIEW +            |')
                    print(line)
                    # A loop to print the content of the dictionary
                    # Each account as key and its corresponding password as value.
                    for i, (k, v) in enumerate(pwd.items(), start=1):
                        print(f'|  {i}. {k} | {v}')
                    print(line)
                else:
                    print(f'The database file does not exist.')
            else:
                print('Invalid choice.')
                continue
        sys.exit(1)

    # LAUNCH THE SCRIPT WITH SOME DEFINED OPTIONS FROM TERMINAL.
    # DEFINE SOME OPTIONS TO TYPE IN DIRECTLY IN THE SHELL.

    # `-a` to add a new password.
    # `-g` to get a password.
    # `-d` to delete a password.
    # `-v` to view all the passwords.

    # Check if the terminal prompt have more than 2 arguments.
    # Launch the script instead : `python pwdm.py -arg`.
    if len(sys.argv) > 2:
        print('\nusage: ./pwdm.py [-a | -g | -d | -v]')
        args = sys.argv[1:]
        # Print out a message to specify invalid options.
        print(f"Options `{' '.join(args)}` are not valid.")
        # Print out the content of the defined manual text file.
        try:
            with open(file2) as f:
                contents = f.read()
                print(contents)
        except:
            # use pass to fail silently.
            #pass
            print('Could not open the manual file.')
        sys.exit(1)

    if len(sys.argv) == 2:
        # Conditions to launch the script with correct arguments.
        option = sys.argv[1]

        if option == '-a':
            add(file1)

        elif option == '-g':
            # First check if the file exists.
            f = found(file1)
            if f == True:
                result = get_pwd(file1)
                account = input('Account to get its password\n: ').title()
                if account in result.keys():
                    pwd = result[account]
                    text = clipboard.copy(pwd)
                    print(line)
                    print('|           + VIEW +            |')
                    print(line)
                    print(f' Account `{account}` found.')
                    print(f' Password `{pwd}` copied to clipboard.')
                    print(line)
                else:
                    print(line)
                    print('|           + VIEW +            |')
                    print(line)
                    print(f' -> Account `{account}` not found.')
                    print(line)
            else:
                print(f'The database file does not exist.')

        elif option == '-d':
            # First check if the file exists.
            f = found(file1)
            if f == True:
                # Call the delete function.
                result = delete(file1)
                account, pwd = result.keys(), result.values()
                # Check if the database file is empty.
                with open(file1) as f:
                    first_char = f.read(1)
                    if not first_char:
                        print(f'`{file1}` is empty.')
                    else:
                        print(f'Data to delete: `{account} : {pwd}`')
                        print('...')
                        time.sleep(0.1)
                        print(f'Account `{account}` successfully deleted.\n')
            else:
                print(f'The database file does not exist.')

        elif option == '-v':
            # First check if the file exists.
            f = found(file1)
            if f == True:
                pwd = view(file1)
                print(line)
                print('|           + VIEW +            |')
                print(line)
                # A loop to print the content of the dictionary
                # Each account as key and its corresponding password as value.
                for i, (k, v) in enumerate(pwd.items(), start=1):
                    print(f'|  {i}. {k} | {v}')
                print(line)
            else:
                print(f'The database file does not exist.')
        else:
            print(f"Unknown option: `{option}`")
            sys.exit(1)

# The standard boilerplate statement to call the main function.
if __name__ == '__main__':
    main()
