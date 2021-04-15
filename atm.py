import random
import validate

database = {}


def init():

    print('Welcome to DEV bank')
    have_account = input('Do yo have account with us: 1. (Yes) 2. (No) \n')
    valid = validate.init_valid(have_account)
    if valid:
        if (int(have_account) == 1):
            login()
        elif (int(have_account) == 2):
            print(register())
        else:
            print('You have selected an invalid option') 
            init()
    else:
        init()


def register():
    global account_number

    print('******************** Register ********************')
    print("********Please enter your correct details*********\n")

    first_name = input('What is your Firstname: \n').capitalize()
    last_name = input('What is your Lastname: \n').capitalize()
    email = input('What is your email address: \n')
    password = input('Create a password for yourself: \n')
    
    
    print("")
    account_number = generate_account_num()
    database[account_number] = [ first_name, last_name, email, password,  ]
    
    print('Your Accout have been created')
    print('====**************************====')
    print('Your account number is: %d' % account_number)
    print('====**************************====')
    
    login()


def login():

    print('')
    account_number_from_user = input('What is your account Number: \n')
    is_valid = validate.account_num_validation(account_number_from_user)

    if is_valid:
        for account_number, detail in database.items():
            if(account_number == int(account_number_from_user)):
                password = input("What is your password \n")
                if(detail[3] == password):
                    bank_operation(detail)
                else:
                    print('Invalid password')
                    login()

            else:
                print('invalid account Number')
                login()
    else:
        init()


def bank_operation(detail):

    print('Welcome {} {}'.format(detail[0], detail[1]))

    selected_option = input('What would you like to do?\n 1. deposit\n 2. withdrawal\n 3. Exit\n ')
    

    try:
        if ( int(selected_option) == 1):
            deposit()

        elif (int(selected_option) == 2):
            withdrawal(account_number)

        elif (int(selected_option) == 3):
            logout()

        else:
            print('Invalid option choosen')
            bank_operation()
            
    except ValueError:
        print('Enter an integer')
        bank_operation(detail)


def deposit():
    global account_number

    balance = 0
    amt_to_deposit = int(input('How much would you like to deposit:  '))
    balance +=amt_to_deposit

    database[account_number].append(balance)
    print(f'Your new balance is {balance}')
    perform()


def withdrawal(account_number):
    withdraw_amt = int(input('How much would you like to withdraw \n'))
    get_balance = int(database[account_number][4])

    if withdraw_amt > get_balance:
        print('Account balance is low')
        withdrawal(account_number)

    elif withdraw_amt < get_balance:
        balance = get_balance - withdraw_amt
        database[account_number].append(balance)
        print('Take your cash')
        print(f'Your Account balance is {balance}')
        perform()


def perform():
    transaction = int(input('Do you want to peform another? 1.Yes 2.No:\n'))

    if (transaction == 1):
        login()

    elif (transaction == 2):
        print(database)
        logout()


def generate_account_num():
    num = random.randrange(1111111111, 9999999999)
    return num


def logout():
    print('Thanks for using our service')
    print(database)

init()