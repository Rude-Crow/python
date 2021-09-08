YearSalary = int(input("Enter yearly salary: £"));

if (YearSalary <= 12500):
    print ("You do not owe any tax (tax free)");
elif (YearSalary <= 50000):
    tax = 20*(YearSalary / 100); # this returns 20% 
    print ("You pay 20% tax. The amount you pay is: " + str(tax));
elif (YearSalary > 50000):
    tax = 40*(YearSalary / 100); # this returns 40% 
    print ("You pay 40% tax. The amount you pay is: " + str(tax));
else:
    print ("an error has occured, please only enter numbers next time");45
