import mysql.connector
import re
import datetime
con = mysql.connector.connect(
  host="127.0.0.1",
  user="admin3",
  password="Passw0rd!",
)
cur = con.cursor()


def Signup():
    #Checks that database and table exist, if they don't it creates them
    cur.execute("CREATE DATABASE IF NOT EXISTS Generation1;")
    cur.execute("USE Generation1;")
    cur.execute("CREATE TABLE IF NOT EXISTS Users (Username VARCHAR(255) NOT NULL, Password VARCHAR(255) NOT NULL, Firstname VARCHAR(255) NOT NULL, Surname VARCHAR(255) NOT NULL, Email_address VARCHAR(255) NOT NULL, Age INT UNSIGNED NOT NULL, SignUpDate DATE NOT NULL, PRIMARY KEY (Username));")

    Signup_Check = False
    while Signup_Check == False: #Does subsequent code until signup_check isn't false
        
        #Username validation using a regex expression
        Username_check = False
        while Username_check == False:
            Username = input("Enter a username: ")
            Valid = re.match(r'^[a-zA-Z0-9\d]+$', Username)
            if Valid:
                Username_check = True
            else:
                Username_check = False
                print("Not valid")

        #Password validation using a regex expression
        Password_check = False
        while Password_check == False:
            Password = input("Enter a password: ")
            Valid = re.match(r'^[a-zA-Z0-9]{1,15}$', Password)
            if Valid:
                Password_check = True
            else:
                Password_check = False
                print("Not valid")

        #First name validation using a regex expression
        Firstname_check = False
        while Firstname_check == False:
            Firstname = input("Enter your first name: ")
            Valid = re.match(r'^[a-zA-Z]{1,15}$', Firstname)
            if Valid:
                Firstname_check = True
            else:
                Firstname_check = False
                print("Not valid")
        
        #Surname name validation using a regex expression
        Surname_check = False
        while Surname_check == False:
            Surname = input("Enter your surname: ")
            Valid = re.match(r'^[a-zA-Z]{1,15}$', Surname)
            if Valid:
                Surname_check = True
            else:
                Surname_check = False
                print("Not valid")

        #Email validation using a regex expression
        Email_check = False
        while Email_check == False:
            Email = input("Enter your email: ")
            Valid = re.match(r'^[a-zA-Z0-9.-_+]+@[a-zA-Z.]{1,15}$', Email)
            if Valid:
                Email_check = True
            else:
                Email_check = False
                print("Not valid")

        #Age validation using a regex expression
        Age_check = False
        while Age_check == False:
            Age = input("Enter your age: ")
            Valid = re.match(r'^[0-9]{1,2}$', Age)
            if Valid and int(Age) > 17:
                Age_check = True
            elif Valid and int(Age) <= 17:
                Age_check = False
                print("Under 18")
            else:
                Age_check = False
                print("Not valid")

        #This gets the current date to input for user profile creation
        Date = datetime.date.today()
        SignUpDate = Date
        
        #This inserts the checked data into the database
        cur.execute(f"INSERT INTO Users VALUES ('{Username}', '{Password}', '{Firstname}', '{Surname}', '{Email}', '{Age}', '{SignUpDate}');")
        con.commit()
        db = cur.fetchall()
        print(db)

        print("You have sucessfully signed up!")

        Signup_Check = True
    
    return()

    
