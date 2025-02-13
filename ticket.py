''' problem set 1 Q3
    
    TICKET COUNTER

	Develop a python program for the Ticket Counter section
	in a gallery for viewing a horror show.
	Children "under 11” and Senior Citizens "equal to and above 75"
	are not eligible to buy the ticket nor view the show.
	Values of age with months should be rounded to the ceil values
	if age is 0.5 and above (Example 1.5 should be rounded as 2) and
	values of age with months should be rounded to floor values,
	if age is less than 0.5 (Example 1.2 should be rounded as 1).
	Following table provides the price for each individual based on their age.
    
	Ticket Price
	11-14  Rs. 250
	15-25  Rs.275
	>25    Rs.300    '''
print(" Hi ")
import math
r,age=0.0,0.0
age=float(input())
if (age<0):
    print(" invalid input ")
else:
    r=(age%1)
    if (r<0.5):
        age=math.floor(age)
    else:
        age=math.ceil(age)
    if (11<=age<=14):
        print(" Rs. 250 ")
    elif (15<=age<=25):
        print(" Rs. 275 ")
    elif (25<age<75):
        print(" Rs. 300 ")
    else:
        print(" not eligible to buy ticket nor view the show. ")
#end of program