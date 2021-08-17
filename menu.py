from database_manager import store_account, find_accounts, find_password



def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Enter all info about site that you want to save')
    print('2. Find all sites and apps connected to an email')
    print('3. Find password for a site or app')
    print('Q. Exit')
    print('-'*30)
    return input('Your choice : ')


def store_password():
   print('-'*30)
   print("please enter all of info that want from you carefully: ")
   print("app_name : ")
   app_name = input()
   print("url : ")
   url = input()
   print("username : ")
   username = input()
   if username == None:
      username = ''
   print("password : ")
   password = input()
   store_account(app_name, url, username, password)

def find_all():
   print('Please proivide the email that you want to find accounts for')
   username = input()
   find_accounts(username)

def find():
   print('Please proivide the name of the site or app you want to find the password to')
   app_name = input()
   find_password(app_name)
