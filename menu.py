from database.database_manager import store_account, find_accounts, find_password
from utils.input_validation import validate_input, validate_app_name, validate_password

def menu():
    """Display the main menu and get user choice."""
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Save account information')
    print('2. Find accounts by username')
    print('3. Find password for an app/site')
    print('Q. Exit')
    print('-' * 30)
    return input('Your choice: ').strip().lower()

def store_password():
    """Prompt the user to enter account information and store it."""
    print('-' * 30)
    print("Please enter the required information:")
    
    app_name = validate_input("App Name: ", validate_app_name)
    url = validate_input("URL: ")
    username = validate_input("Username: ")
    password = validate_input("Password: ", validate_password)

    store_account(app_name, url, username, password)

def find_all():
    """Find all accounts associated with a username."""
    username = validate_input("Enter the username to search for: ")
    find_accounts(username)

def find():
    """Find the password for a specific app/site."""
    app_name = validate_input("Enter the app/site name to find the password: ")
    find_password(app_name)