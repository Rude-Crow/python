import math

NumberOfStudents = int(input("Enter number of students: "));
NumberOfBusses = math.ceil(NumberOfStudents / 42);
print ("Number of busses needed: " + str(NumberOfBusses));