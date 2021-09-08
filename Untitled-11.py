Word = input("Enter word: ")
Count = 0
Vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

if Word:
    for letter in Word:
        if letter == "A" or letter == "a" or letter == "E" or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" or letter == "U" or letter == "u":
        #if letter == list(Vowels): 
            Count += 1
            print (Count , letter)

else:
    print("Error!") 