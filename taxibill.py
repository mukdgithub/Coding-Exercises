''' Write a Python program to accept the kilometers traveled by Mr. Roy 
    and calculate his taxi bill.
    
           First 10 Km        Rs 15/km
           Next 90 Km         Rs  8/km
           After that         Rs  6/km

	module 3 workout Q2 '''

km,bill=0,0
km=int(input())
if km<=10:
    bill=(km*15)
elif km<=100:
    bill=(150+((km-10)*8))
else :
    bill=(150+720+((km-100)*6))

print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')

print(bill)

# end of program