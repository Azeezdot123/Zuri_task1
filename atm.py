import random
import datetime

time = datetime.datetime.now()
database = {}


def init():

    print('Welcome to DEV bank')
    have_account = int(input('Do yo have account with us: 1. (Yes) 2. (No) \n'))
    if (have_account == 1):
        login()
    elif (have_account == 2):
        print(register())
    else:
        print('You have selected an invalid option') 
        init()


def login():

    print('')
    accountNumberFromUser = int(input('What is your account Number: \n'))

    for accountNumber,value in database.items():
        
        if(accountNumber == accountNumberFromUser):
            password = input("What is your password \n")
            if(value[3] == password):
                bankOperation(value)
            else:
                print('Invalid password')
                login()

        else:
            print('invalid account Number')
            login()


def register():

    print('******************** Register ********************')
    print("********Please enter your correct details*********\n")

    firstName = input('What is your Firstname: \n').capitalize()
    lastName = input('What is your Lastname: \n').capitalize()
    email = input('What is your email address: \n')
    password = input('Create a password for yourself: \n')
    
    print("")
    accountNumber = generateAccountnum()
    database[accountNumber] = [ firstName, lastName, email, password ]

    print('Your Accout have been created')
    print('====**************************====')
    print('Your account number is: %d' % accountNumber)
    print('====**************************====')
    
    login()


def bankOperation(value):

    print('Welcome {} {}'.format(value[0], value[1]))

    selectedOption = int(input('What would you like to do?\n 1. deposit\n 2. withdrawal\n 3. Exit\n '))

    if ( selectedOption == 1):
        deposit()

    elif (selectedOption == 2):
        withdrawal()

    elif ( selectedOption == 3):
        logout()

    else:
        print('Invalid option choosen')
        bankOperation()


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

def logout():
    print('Thanks for using our service')
    pass

init()