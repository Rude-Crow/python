Passed_test = bool(input("Did you pass your test: "))
Current_year_group = int(input("What year group are you in: "))
Test_exempt = bool(input("Are you test exempt: "))


if not Passed_test == True or not Test_exempt == True:
    print("Student must retake test.")
elif Passed_test == True and Current_year_group >= 11 or Test_exempt == True and Current_year_group >= 11:
    print("Congratulations you have graduated!")
elif Passed_test == True and Current_year_group <= 11 or Test_exempt == True and Current_year_group <= 11:
    print("Congratulations on passing your end of term see you next year!")
else:
    print("You haven't passed you must retake the test.")
