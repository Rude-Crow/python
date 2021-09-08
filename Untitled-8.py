Word = input("Enter a word: ");
FirstLetter = str(Word[0:1]);
CapitalCheck = FirstLetter.isupper();

if (CapitalCheck == True):
    print("The first letter is uppercase.");
elif (CapitalCheck == False):
    print("The first letter is lowercase.");
else:
    print("Error, please try again and only enter letters for the word.")