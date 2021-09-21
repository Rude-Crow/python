import mysql.connector
con = mysql.connector.connect(
  host="127.0.0.1",
  user="admin3",
  password="Passw0rd!",
)
cur = con.cursor()


def Login():# login function
    cur.execute("USE Generation1;") #makes sure database in use is generation1
    Login = False
    while Login != True: #boolean loop 
        Username = input("Enter your username:\n") 
        cur.execute(f"""SELECT Password FROM Users WHERE Username='{Username}'""") #mysql search gets password using Username
        Valid = cur.fetchone() #saves password
        if Valid:
            LogOut = False
            while LogOut != True:
                Password = input("Enter your password:\n")
                if Password == Valid[0]: #checks the searched for password against the users entered one if invalid loops
                    cur.execute(f"""SELECT Firstname FROM Users WHERE Username='{Username}'""")#gets info from the table to return to main for display
                    firstname = cur.fetchone()
                    cur.execute(f"""SELECT Surname FROM Users WHERE Username='{Username}'""")
                    surname = cur.fetchone()
                    cur.execute(f"""SELECT Email_address FROM Users WHERE Username='{Username}'""")
                    email = cur.fetchone()
                    cur.execute(f"""SELECT Age FROM Users WHERE Username='{Username}'""")
                    age = cur.fetchone()
                    return(firstname, surname, age, email)#returns with these valuse to main

                else:
                    print("Invalid Password")
        else:
            print("invalid User")