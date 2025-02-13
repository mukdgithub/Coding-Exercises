''' Construct a python program to accept the yearly income of an employee
    and display the income tax to be paid at the end of the year
    according to the following criteria
    
    Annual income (in Rs)           Income Tax
     > 1000000                        4 %
     > 500000 and <= 1000000          2 %
     <= 500000                        NIL
    
    module 3 workout Q1   '''

income,tax=0.0,0.0
income=float(input())
if income>1000000:
    tax=(0.04*income)
elif income>500000:
    tax=(0.02*income)
else :
    tax=0

print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')

print(tax)

# end of program