import sqlite3
import traceback
import sys

def connect_database():
    try:
        Connection = sqlite3.connect('Pass_Manager.db')
        cursor = Connection.cursor()
        
        db_create_table = '''CREATE TABLE IF NOT EXISTS pass_manager (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            app_name text,
                            url text,
                            username text,
                            password text);'''
        cursor.execute(db_create_table)
        return Connection

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

def store_account(app_name, url, username, password):
    try:
        Connection = connect_database()
        cursor = Connection.cursor()
        print("Successfully Connected to SQLite")

        db_store_account =  "INSERT INTO pass_manager VALUES (null, ?, ?, ?, ?)"
        db_record_to_insert = (app_name, url, username, password)
        cursor.execute(db_store_account, db_record_to_insert)
        Connection.commit()
        print('your info about your account has beed saved. Good luck!')
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table")
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))


def find_accounts(username):
    try:
        Connection = connect_database()
        cursor = Connection.cursor()
        cursor.execute("SELECT * FROM pass_manager WHERE username=?", [username])
        result = cursor.fetchall()
        print(result)
        print('RESULTS')
        print('')
        for item in result:
            print(f'{item[0]}th row: \napp name: {item[1]}\nurl: {item[2]}\nusername: {item[3]}\npassword: {item[4]}')
            print('-'*30)
        
    except Exception as error:
        print(error)

def find_password(app_name):
    try:
        Connection = sqlite3.connect('Pass_Manager.db')
        cursor = Connection.cursor()
        cursor.execute("SELECT password FROM pass_manager WHERE app_name=?", [app_name])
        result = cursor.fetchone()
        for password in result:
            print(f'passord of {app_name} is : {password}')
    except sqlite3.Error as error:
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))


