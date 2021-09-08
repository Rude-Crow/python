import random #imports random library

def Game():
    Userguess = 0
    Win = False
    RadNumber = random.randrange(0,101) #gets random number
    Attempt = 0

    while Win != True: #while win isn't true this code loops
        Userguess = int(input("Enter guess: "))#gets user guess
        Attempt += 1
        Win, Message = NumCheck(Userguess, RadNumber, Attempt)
        print(Message)
    return
        

def NumCheck(Userguess, Number, Attempts):
    if Userguess == Number:#checks user guess if same as random number
        return True, "Congrats! You won in " + str(Attempts) + " attempts."#displays number of user attempts at guessing 
    elif Userguess < Number :#checks user guess is lower than random number
        return False, "Too low! Try again!"
    elif Userguess > Number :#checks user guess is higher than random number
        return False, "Too high! Try again!"

def Main():
    Game()

Main()