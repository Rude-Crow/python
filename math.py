"""Write a function that takes two numbers and a mathematical operator. 
Return the correct answer. E.g. 2, 3, + would return 5. Where as 2, 3, * would return 6. """

def Math(Num1, Oper, Num2): #Declare function called math
    if Oper == "+": #If and elif to check for operator
        Ans = int(Num1) + int(Num2)
        return Ans #Returns answer of equation
    elif Oper == "-":
        Ans = int(Num1) - int(Num2)
        return Ans
    elif Oper == "*":
        Ans = int(Num1) * int(Num2)
        return Ans
    elif Oper == "/":
        Ans = int(Num1) / int(Num2)
        return Ans
    else:
        return print("Error: You didn't input a math operator")

Number1 = input("Enter a number: ")
MOperator = input("Enter a math operator (+-/*): ")
Number2 = input("Enter a number: ")
Equation = str(Number1) + " " + str(MOperator) + " " + str(Number2) #combines entered varibles into string for output sentance
Answer = Math(Number1, MOperator, Number2) #gets the returned value from the math function
print("Your answer to " + str(Equation) + " is " + str(Answer)) #Outputs answer