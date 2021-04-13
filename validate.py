def account_num_validation(account_number):

    if account_number:

        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True

            except ValueError:
                print('Invalid account number, account should be a Number')
                return False

        else:
            print('Account Number cannot be more or less than 10 digit')
            
    else:
        print('Account Number is required')
        return False

def init_valid(have_account):
    try:
        int(have_account)  
        return True
    except ValueError:
        print('Enter an integer')
        return False
        
def validate_registration():
    pass