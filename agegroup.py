""" classification based on age entered
    it is called table problem """

age=0
age=float(input(" Enter the Age : "))
if (age<18):
    print(" Minor ")
elif (18<=age<30):
    print(" Youth ")
elif (30<=age<50):
    print(" Middle ")
elif (50<=age):
    print(" Senior Citizen ")
#end of program