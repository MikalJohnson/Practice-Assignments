# Sign up
# A. Ask user to enter a preferred username
username = input("Enter a username: ")
# B. Ask user to enter a preferred password
password = input("Enter a password: ")

#Login
login = 'n'
while login == 'n':
    # Ask user to login with their username and password
    loginname = input("Enter the username you created to login: ")
    loginpass = input("Enter the password you created to login: ")

    if loginname == username and loginpass == password:
        print("Login successful and exit the program")
        login = 'y'
    else:
        print("Login failed, please enter the correct username or password")