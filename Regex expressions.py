import re

def PasswordChecker(): #defines function called PasswordChecker 
    passwd = input("Enter a password to check: ") #Gets user input
    passwd_check = re.match(r'^[a-zA-Z0-9@#$%^&+=]{1,8}$', passwd) #creates an expression to check against
    if passwd_check:
        print('Valid')
    else:
        print('Invalid')

def LicenseChecker(): #defines function called LicenseChecker
    license = input("Enter a license plate to check: ") #Gets user input
    validLicense = re.match(r'^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$', license) #creates an expression to check against
    if validLicense:
        print('Valid')
    else:
        print('Invalid')

def WebAddressChecker(): #defines function called WebAddressChecker
    WebAddress = input("Enter a web address to check: ") #Gets user input
    WebAddressCheck = re.match(r'^(www.)?[a-zA-Z0-9]+.[a-zA-Z.]{1,5}$', WebAddress) #creates an expression to check against
    if WebAddressChecker:
        print('Valid')
    else:
        print('Invalid')

def PrivIPCheck(): #defines function called PrivIPCheck
    IP = input("Enter a private IP address to check: ") #Gets user input
    IPCheck = re.match(r'(^127\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)', IP) #creates an expression to check against
    if IPCheck:
        print('Valid')
    else:
        print('Invalid')

#PasswordChecker()
#LicenseChecker()
#WebAddressChecker()
PrivIPCheck()