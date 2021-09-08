import datetime

def WritePost(blogPost1): #function to write blog post that includes author, date, blog title and blog content.
    key = "Author"
    value = input("Enter your name: ")
    blogPost1[f'{key}'] = value # the first three lines create a dictionary entry with the key "Author".
    key = "Date"
    date = datetime.date.today()
    value = str(date)
    blogPost1[f'{key}'] = value # the next four lines create a dictionary entry with the key "Date".
    key = "Title"
    value = input("Enter your blog title: ")
    blogPost1[f'{key}'] = value # these three lines create a dictionary entry with the key "Title".
    key = "Content"
    value = input("Enter your blog content: ")
    blogPost1[f'{key}'] = value # the last three lines create a dictionary entry with the key "Content".
    return blogPost1 #This returns the new entered data.

def BlogDisplay(blogPost1): #This function prints the blog in a user friendly format, using .get to obtain the associated information to the keys.
    print ("Author: " + blogPost1.get('Author') + "\nDate: " + blogPost1.get('Date') + "\nTitle: " + blogPost1.get('Title') + "\nContent: " + blogPost1.get('Content'))



def UpdatePost(blogPost1): #this function allows the user to update all fields of the blog post.
    blogPost1['Author'] = input('Enter updated author name: ')
    date = datetime.date.today()
    value = str(date)
    blogPost1['Date'] = value
    print('Enter updated date in YYYY-MM-DD format: ')
    blogPost1['Title'] = input('Enter updated blog title: ')
    blogPost1['Content'] = input('Enter updated blog content: ')
    return blogPost1

def MakeAListToDict(): #this function allows the user to enter information via a list and then converts that list into a dictionary.
    List = [] #creates empty list
    x = 0
    EntryNum = int(input("How many entries: ")) #allows user to decide how many entries to the list they want to make.
    while x < EntryNum: #this while loop allows the user to enter info for the list as many times as they decided.
        Key = input("Enter key: ")
        Value = input("Enter value: ")
        List.append([Key, Value]) #this appends the information entered to the list.
        x += 1
    NewDict = {} #creates empty dictionary.
    for row in List: #does a loop for every entry in the list.
        key = row[0] #takes first part of the entry as the key.
        value = row[1] #takes second part of the entry as the value/ associated content.
        NewDict[f'{key}'] = value #Enters converted information to the dictionary. 
    return NewDict



def main():
    blogPost1 = {}
    blogPost1 = WritePost(blogPost1)
    BlogDisplay(blogPost1)
    UpdatedBlogPost1 = UpdatePost(blogPost1)
    NewDict = MakeAListToDict()
    print(NewDict)

main()