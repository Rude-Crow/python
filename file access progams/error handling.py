
b = 0

while b != 1:
    try:
        a = 1/0

    except Exception as error:
        file = open("file access progams/error.txt", "a") #opens file in append mode
        e = str(error) #sets the error to a string in a varible to print
        file.write("\n" + e) #writes the varible to the txt file
        file.close() #closes the file
        continue

    finally:
        print("you had an error")
        break

