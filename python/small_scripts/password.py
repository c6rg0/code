import string
usernameSave = "gabriel"
passwordSave = "Hello1!"
count = 0

#SUBPROGRAMS

def menu():
    selection = int(input("Do you want to login(1), sign-up(2) or reset(3) your password: "))
    if selection == 1:
        login_account()
        
    """if selection == 2:
        create_account"""

    if selection == 3:
        password_reset()

    
def check_string(s):
    has_upper = any(char.isupper() for char in s)
    has_lower = any(char.islower() for char in s)
    has_digit = any(char.isdigit() for char in s)
    has_symbol = any(not char.isalnum() for char in s)

    return has_upper, has_lower, has_digit, has_symbol


def login_account():
    print()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == usernameSave:
        if password == passwordSave:
            print("Logged in!!!")
        else:
            print("Incorect password, try again")
            count = count + 1
            if count == 3:
                password_help()
                login_account()

"""def create_account():"""
    

def password_help():
    print("Incorect password, you taken a lot of tries.")
    menu()

def password_reset():
    print()
    username = input("Enter your username: ")
    if username == usernameSave:
        print("Password has to be at least 7 characters.")
        print("It must contain an upercase, lowercases, number and a symbol.")
        newPassword1 = input("Enter new password: ")
        newPassword2 = input("Repeat new password: ")
        if newPassword1 == newPassword2:
            string = newPassword1
            result = check_string(string)
            if False in result:
                print("The password doesn't include one of the requirements, please try again.")
                password_reset()
            else:
                passwordSave = string
                print("The password has been set")
                menu()

#MAIN PROGRAM
            
menu()
