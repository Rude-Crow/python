import random #imports random library

RadNumber = random.randrange(0,101) #gets random number
Attempts = 0
Userguess = 0
Win = False

while Win != True: #while win isn't true this code loops
    Number = int(RadNumber)
    Userguess = int(input("Enter guess: "))#gets user guess
    Attempts += 1#adds 1 to attempt
    if Userguess == Number:#checks user guess if same as random number
        Win = True #sets win to true ending loop
    elif Userguess < Number :#checks user guess is lower than random number
        print("Too low! Try again!")
    elif Userguess > Number :#checks user guess is higher than random number
        print("Too high! Try again!")

print("Congrats! You won in " + str(Attempts) + " attempts.")#displays number of user attempts at guessing 




