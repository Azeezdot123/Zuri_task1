import random
import datetime

time = datetime.datetime.now()
database = {}


def init():

    print('Welcome to DEV bank')
    have_account = input('Do yo have account with us: 1. (Yes) 2. (No) \n')
    valid = init_valid(have_account)
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


def login():

    print('')
    accountNumberFromUser = input('What is your account Number: \n')
    is_valid = accountNumValidation(accountNumberFromUser)

    if is_valid:
        for accountNumber,value in database.items():
            if(accountNumber == int(accountNumberFromUser)):
                password = input("What is your password \n")
                if(value[3] == password):
                    bankOperation(value)
                else:
                    print('Invalid password')
                    login()

            else:
                print('invalid account Number')
                login()
    else:
        init()


def accountNumValidation(accountNumber):
    if accountNumber:
        if len(str(accountNumber)) == 10:
            try:
                int(accountNumber)
                return True
            except ValueError:
                print('Invalid account number, account should be a Number')
                return False
        else:
            print('Account Number cannot be more or less than 10 digit')
    else:
        print('Account Number is required')
        return False


def register():

    print('******************** Register ********************')
    print("********Please enter your correct details*********\n")

    first_name = input('What is your Firstname: \n').capitalize()
    if first_name:
        last_name = input('What is your Lastname: \n').capitalize()
        if last_name:
            email = input('What is your email address: \n')
            if email:
                password = input('Create a password for yourself: \n')
                if password == "":
                    print('Enter a password')
                    register()
            else:
                register()
        else:
            register()
    else:
        register()
    
    print("")
    accountNumber = generateAccountnum()
    database[accountNumber] = [ first_name, last_name, email, password ]

    print('Your Accout have been created')
    print('====**************************====')
    print('Your account number is: %d' % accountNumber)
    print('====**************************====')
    
    login()


def bankOperation(value):

    print('Welcome {} {}'.format(value[0], value[1]))

    selectedOption = input('What would you like to do?\n 1. deposit\n 2. withdrawal\n 3. Exit\n ')
    

    try:
        if ( int(selectedOption) == 1):
            deposit()

        elif (int(selectedOption) == 2):
            withdrawal()

        elif (int(selectedOption) == 3):
            logout()

        else:
            print('Invalid option choosen')
            bankOperation()
            
    except ValueError:
        print('Enter an integer')
        bankOperation(value)


def deposit():
    depositAmt = 0
    userDeposit = int(input("How much would you like to deposit \n"))
    depositAmt += userDeposit
    print( 'Your new balance is %s'% depositAmt)
    perform()


def withdrawal():
    withdraw_amt = int(input('How much would you like to withdraw \n'))
    print('Take you cash')
    print(f'Your withdrawal amount is {withdraw_amt}')
    perform()


def generateAccountnum():
    num = random.randrange(1111111111, 9999999999)
    return num

def perform():
    transaction = int(input('Do you want to peform another? 1.Yes 2.No:\n'))

    if (transaction == 1):
        login()

    elif (transaction == 2):
        logout()

def init_valid(have_account):
    try:
        int(have_account)  
        return True
    except ValueError:
        print('Enter an integer')
        return False
        
def logout():
    print('Thanks for using our service')
    pass

init()