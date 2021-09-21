import signup
import login


def Main():
    choice = input("Do you want to login (l/L) or sign up (s/S):\n") #Allows you to select to sign up or login
    if choice == "L" or choice == "l":#checks choice
        firstname, surname, age, email = login.Login()#goes to module login for login function
        print("Name: ", firstname[0], surname[0])
        print("Age: ", age[0])
        print("Email: ", email[0])
    elif choice == "S" or choice == "s":#checks choice
        signup.Signup()#goes to module signup for signup function
    else:
        print("You have entered an incorrect choice please choose again.")
        Main()

Main()
