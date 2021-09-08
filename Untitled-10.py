x = int(input("Enter a number between 1 and 30: "))

if x >= 1 and x <= 30:
    for z in range(x):
        print("I do love potatoes!")
elif x < 1:
    x = 1
    print("you entered a number lower than 1 so your choice has been set to 1.")
    for z in range(x):
        print("I do love potatoes!")
elif x > 30:
    x = 30
    print("you entered a number higher than 30 so your choice has been set to 30.")
    for z in range(x):
        print("I do love potatoes!")
else:
    print("Error! Did you enter a number?")
