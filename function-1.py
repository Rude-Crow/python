# Write a function that does not take any information, but when it's called it provides a welcome message to the user. 
# Update the function above so that it now takes a name for the user as a parameter when it is called, use this name in the welcome message
"""Write a function that takes two names, a person's first name and last name, as parameters when the function is called. 
Use these two names to create a new variable called ‘fullName’. Print a welcome message using their full name. """

def WelcomeUser (FName, SName): #creates a function called WelcomeUser
    FullName = FName + " " + SName #Adds the two strings together with a space
    print("Welcome " + FullName + "!")


FirstName = input("Enter your first name: ")
SecondName = input("Enter your surname name: ")
WelcomeUser(FirstName, SecondName) #Calls function WelcomeUser and passes varible MyName