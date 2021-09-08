#1 = rock
#2 = scissors
#3 = paper

import random #imports random library

def Outcome(UserTurn, CompTurn): #Comparing results function
#User Wins
    if UserTurn == 1 and CompTurn == 2 or UserTurn == 2 and CompTurn == 3 or UserTurn == 3 and CompTurn == 1:
        return "The User Wins", 1

#Computer Wins
    elif UserTurn == 1 and CompTurn == 3 or UserTurn == 2 and CompTurn == 1 or UserTurn == 3 and CompTurn == 2:
        return "The CPU Wins", 2

#Draw
    else: #UserTurn == 1 and CompTurn == 1 or UserTurn == 2 and CompTurn == 2 or UserTurn == 3 and CompTurn == 3: #user rock, CPU rock
        return "it's a draw", 0
    
def CompInput(): #Computer input function
  CompTurn = random.randrange(1,4)
  if CompTurn == 1 : #rock
    return 1, "the CPU chose rock"
  elif CompTurn == 2: #scissors
   return 2, "the CPU chose scissors"
  elif CompTurn == 3: #paper
    return 3, "the CPU chose paper"
  else:
    return "Invalid"

def UserInput(): #User input function
  UserTurn = input ("Choose rock, paper, or scissors: ").lower()
  if UserTurn == "rock":
    return 1, "the User chose rock"
  elif UserTurn == "scissors":
    return 2, "the User chose scissors"
  elif UserTurn == "paper":
    return 3, "the User chose paper"
  else:
    return "Invalid input"
    UserInput()


def Main(): #Main function that calls on other functions
  UserWin = 0
  CompWin = 0
  Draw = 0
  Games = 0
  while UserWin < 2 and CompWin < 2 and Draw < 3 and Games < 3: #while loop checking to see best of 3
    UserTurn, UserPick = UserInput() #Returns info from UserTurn
    CompTurn, CompPick = CompInput() #Returns info from CompTurn
    Out = Outcome(UserTurn, CompTurn)[0] #gets first returned value of outcome
    Win = Outcome(UserTurn, CompTurn)[1] #gets second returned value of outcome
    print (str(Out) + ", " + str(UserPick) + ", " + str(CompPick))
    if Win == 1:
      UserWin += 1
      Games += 1
    elif Win == 2:
      CompWin += 1
      Games += 1
    elif Win == 0:
      Draw += 1
      Games += 1
    else:
      print("Error!")
  
  if UserWin == 2 or UserWin == 1 and Draw == 2: #Listing all win/draw conditions
    print("You won the best of three")
  elif Draw == 3 or UserWin == 1 and CompWin == 1 and Draw == 1:
    print("You drew")
  else:
    print ("You lost the best of three")
    
  
  Continue = input("Exit or Continue?: ").lower()
  if Continue == "exit":
    exit
  elif Continue == "continue":
    Main()
  else:
    print("No decision")
    exit

Main()