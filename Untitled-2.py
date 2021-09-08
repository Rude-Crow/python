YourName = input();
YourAge = input();
YourTown = input();
YourDrivTest = input();
DrivTest = "";

print (YourName);
print (YourAge);
print (YourTown);

if YourDrivTest == "yes" or "Yes" or "true" or "True":
    DrivTest == "True"
elif YourDrivTest == "no" or "No" or "false" or "False":
    DrivTest == "False"
else:
    DrivTest == "False";

print ("Hi " + YourName + " so you're " + YourAge + ", from " + YourTown + " and it's " + DrivTest + " That you have passed your driving test.");

