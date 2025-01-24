from menu import menu, store_password, find_all, find

def main():
    while True:
        choice = menu()
        if choice == '1':
            store_password()
        elif choice == '2':
            find_all()
        elif choice == '3':
            find()
        elif choice == 'q':
            print("Exiting the password manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()