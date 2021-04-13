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

    print('******************** Register ********************')
    print("********Please enter your correct details*********\n")

    first_name = input('What is your Firstname: \n').capitalize()
    last_name = input('What is your Lastname: \n').capitalize()
    email = input('What is your email address: \n')
    password = input('Create a password for yourself: \n')
    
    print("")
    account_number = generate_account_num()
    database[account_number] = [ first_name, last_name, email, password, 0 ]

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
            withdrawal()

        elif (int(selected_option) == 3):
            logout()

        else:
            print('Invalid option choosen')
            bank_operation()
            
    except ValueError:
        print('Enter an integer')
        bank_operation(detail)

def set_current_balance(detail, balance):
    balance = detail[4]
    return balance

# def get_current_balance(detail):
#     return database[detail][0]

def deposit():
    
    current_balance = set_current_balance(balance)
    print(current_balance)

    user_deposit = int(input("How much would you like to deposit \n"))

    current_balance += user_deposit
    print(f'Your new balance is {current_balance}')
    perform()

def withdrawal():
    pass

    #get current balance
    #get amount to withdraw
    #check if current balance >withdraw amt
    #deduct withdraw amount from current balance
    #display current balance

    # withdraw_amt = int(input('How much would you like to withdraw \n'))
    # print('Take you cash')
    # print(f'Your withdrawal amount is {withdraw_amt}')
    # perform()

def perform():
    transaction = int(input('Do you want to peform another? 1.Yes 2.No:\n'))

    if (transaction == 1):
        login()

    elif (transaction == 2):
        logout()


def generate_account_num():
    num = random.randrange(1111111111, 9999999999)
    return num









def logout():
    print('Thanks for using our service')
    print(database)

init()