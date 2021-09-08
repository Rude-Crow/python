"""Write a function that takes an integer, and then works out 10% of that number, 15% of that number and 35% of that number. 
The three values should be returned and then stored in separate variables outside the function. """


def percent(Num): #defines function called percent
    Num = int(Num)
    Ten_per= Num / 10 #
    Fithteen_per= 15*(Num/100)
    Thirtyfive_per= 35*(Num/100)
    return (Ten_per, Fithteen_per, Thirtyfive_per) # returns answers

Number = input("Enter a number: ")
Number1 = percent(Number)[0]#Returns first value
Number2 = percent(Number)[1]#Returns second value
Number3 = percent(Number)[2]#Returns third value
print ("Ten perceent is: " + str(Number1) + "\nFithteen percent is: " + str(Number2) + "\nThirtyfive percent is: " + str(Number3))#outputs answers