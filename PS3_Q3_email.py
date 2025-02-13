''' Write a python program for validating email using regular constructs 
	or regular expression. '''

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(email):
    if(re.fullmatch(regex,email)):
        print("Valid Email")
    else:
        print("Invalid Email")
email=input()

print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')

check(email)

# end of program