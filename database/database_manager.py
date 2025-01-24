import sqlite3
import traceback
import sys
from cryptography.fernet import Fernet

# Generate a key for encryption (store this securely in production)
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

def connect_database():
    """Connect to the SQLite database and create the table if it doesn't exist."""
    try:
        connection = sqlite3.connect('Pass_Manager.db')
        cursor = connection.cursor()
        
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS pass_manager (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            app_name TEXT NOT NULL,
            url TEXT,
            username TEXT,
            password TEXT NOT NULL
        );
        '''
        cursor.execute(create_table_query)
        return connection

    except sqlite3.Error as error:
        print("Error while connecting to SQLite:", error)
        raise

def encrypt_data(data):
    """Encrypt sensitive data before storing it in the database."""
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data):
    """Decrypt data retrieved from the database."""
    return cipher_suite.decrypt(encrypted_data).decode()

def store_account(app_name, url, username, password):
    """Store account information in the database."""
    try:
        with connect_database() as connection:
            cursor = connection.cursor()
            encrypted_password = encrypt_data(password)
            insert_query = "INSERT INTO pass_manager (app_name, url, username, password) VALUES (?, ?, ?, ?)"
            cursor.execute(insert_query, (app_name, url, username, encrypted_password))
            connection.commit()
            print("Your account information has been saved successfully!")

    except sqlite3.Error as error:
        print("Failed to insert data into SQLite table:", error)
        traceback.print_exc()

def find_accounts(username):
    """Retrieve all accounts associated with a username."""
    try:
        with connect_database() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM pass_manager WHERE username=?", (username,))
            results = cursor.fetchall()

            if not results:
                print("No accounts found for the provided username.")
                return

            print("\nRESULTS:")
            for row in results:
                decrypted_password = decrypt_data(row[4])
                print(f"{row[0]}th row: \nApp Name: {row[1]}\nURL: {row[2]}\nUsername: {row[3]}\nPassword: {decrypted_password}")
                print('-' * 30)

    except sqlite3.Error as error:
        print("Error while retrieving data:", error)
        traceback.print_exc()

def find_password(app_name):
    """Retrieve the password for a specific app/site."""
    try:
        with connect_database() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT password FROM pass_manager WHERE app_name=?", (app_name,))
            result = cursor.fetchone()

            if result:
                decrypted_password = decrypt_data(result[0])
                print(f"Password for {app_name} is: {decrypted_password}")
            else:
                print(f"No password found for {app_name}.")

    except sqlite3.Error as error:
        print("Error while retrieving password:", error)
        traceback.print_exc()