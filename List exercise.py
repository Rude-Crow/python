def ReplaceName(UserList):
    SearchName = input("Enter the name you would like to change: ")
    ChangeName = input("Enter the name you want to change to: ")
    for index, item in enumerate(UserList):
        if item == SearchName:
            UserList[index] = ChangeName
    print (UserList)


    
def GetInfo(UserList):
    x = 0
    EntryNum = int(input("How many enteries: "))
    while x < EntryNum:
        Name = input("Enter Name: ")
        Age = int(input("Enter Age: "))
        Height = int(input("Enter Hight(cm): "))
        UserList.append([Name, Age, Height])
        x += 1
    return UserList
    

def SortList(UserList):
    list = sorted(UserList)
    print (list.index[0])

def FindUser(UserList):
    SearchName = input("Enter the name you would like to find: ")
    for index, item in enumerate(UserList):
        if item == SearchName:
            print("Name: " + str(UserList[index,0]) + "\nAge: " + str(UserList[index,1]) + "\nHeight: " + str(UserList[index,2]))

def AvgUserAge(UserList):
    AddAge = 0
    for index in UserList:
        AddAge += index[1]
    AvgAge = AddAge / len(UserList)
    print (AvgAge)

def HeightDiff(UserList):
    Tall = UserList[0][2]
    Short = UserList[0][2]
    
    for row in UserList:
        if row[2] > Tall:
            Tall = row[2]
        
        elif row[2] < Short:
            Short = row[2]
    
    diff = int(Tall) - int(Short)
    print('The height difference between the tallest and shortest is: ' + str(diff))

def Eldest(UserList):
    UserList.sort()
    for x in range(3):
        print(UserList[x])

  
def Main():
    UserList = []
    GetInfo(UserList)
    print(UserList)
    #SortList(UserList)
    ReplaceName(UserList)
    #FindUser(UserList)
    #AvgUserAge(UserList)
    #HeightDiff(UserList)
    #Eldest(UserList)
  
Main()