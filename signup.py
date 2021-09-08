Account_check = False
while Account_check == False: #Does subsequent code until Account_check isn't false
    Username = input("Enter a username: ")
    Passwd = input("Enter a password: ")
    Email = input("Enter an email: ")
    if len(Username) >=5 and len(Username)<=10: #checks if the username is between 5 and 10 characters long
        if len(Passwd)>=6 and len(Passwd)<=12: #checks if password is between 6 and 12 characters long
            if Email: #checks that something has been entered
                Account_check = True #makes Account_check no longer False ending the while loop
                print("Successful sign up!")
            else:
                print("Error: please enter an email!")
        else:
            print("Error: please enter a password between 6 to 12 characters long.")
    else:
        print("Error: please enter a username beteen 5 to 10 characters long.")


Attempts = 0
Login = False
while Login == False: #Does subsequent code until Login isn't false
    if Attempts < 5: #Does subsequent code until 5 attempts have passed
        Attempts += 1 #adds 1 to the attempt count
        log_user = input("Enter username: ")
        log_passwd = input("Enter password: ")
        if log_user == Username: #checks the login username against the correct username
            if log_passwd == Passwd: #checks the login password against the correct password
                Login = True #makes Login no longer False ending the while loop
        else:
            print("Incorrect sign in attempt: " + str(Attempts))#displays number of incorrect attempts

    else:
        print("You have attempted to login " + str(Attempts) + "times.")
        exit

print("You have successfully logged in!")
print("Login attempts: " + str(Attempts))