Name = input("Enter name: ");
Surname = input("Enter surname: ");
Byear = input("Enter birth year: ");

username = str(Name[0:1] + Surname + Byear[2:4]);
print ("Your username is: " + username);