from menu import menu, store_password, find_all, find

choice = menu()
while choice != 'q':
    if choice == '1':
        store_password()
    if choice == '2':
        find_all()
    if choice == '3':
        find()
    else:
        choice = menu()
exit()
