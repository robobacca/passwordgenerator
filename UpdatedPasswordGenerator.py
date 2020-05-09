import string
import random

def generate(password_length):
    all_types = string.ascii_letters + string.digits + string.punctuation
    no_sc = string.ascii_letters + string.digits
    letters_only = string.ascii_letters
    
    if user_input_option == 1:
        return ''.join(random.choice(all_types) for i in range(password_length))
    elif user_input_option == 2:
        return ''.join(random.choice(no_sc) for i in range(password_length))
    elif user_input_option == 3:
        return ''.join(random.choice(letters_only) for i in range(password_length))
    
if __name__ == "__main__":
    try:
        print('Welcome to the password generator!')
        start = input('Type \'begin\' to start and cancel to cancel\n')
        if start == 'begin':
            user_input_option = int(input('Please select an option :\n 1. All characters\n 2. Only letters and numbers\n 3. Only letters\n'))
            if user_input_option >= 4 or user_input_option <=0:
                print('Incorrect input. Please try again')
            else:
                password_length = int(input('Please input the desired length of your password\n'))
                try:
                    if password_length < 6:
                        print('password length is not long enough. Please try again.')
                    if password_length > 20:
                        print('password length is too long. Please try again.')
                    else:
                        print('Your password is :',generate(password_length),'\nThank you and don\'t forget to save the password!')
                except ValueError: 
                    print('Input is not an integer, Please try again.')
        else:
            print('Invalid input. Please try again')
    except KeyboardInterrupt:
        print('Program cancelled. Have a nice day.')
            
   
