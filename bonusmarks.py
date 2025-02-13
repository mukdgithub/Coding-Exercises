''' Construct a python program to for the course BCSE101E,
    bonus marks are awarded to the students ,
    according to their mark scored in the exam and the class type.
    Write a python program to accept the marks,
    class type ‘T’ for theory or ‘L’ for lab.
    Display the final marks by adding the bonus mark to the original mark,
    based on the given conditions.
    [Note: If the mark given by the user is 0
    then display the message: “Enter appropriate Mark”].
    
    ...module 3 workout Q3...'''

m,t,bm=0,"",0
m=float(input())
if (m==0):
    print("Enter the appropriate mark")
else :
    t=str(input())
    if (t=="T"):
        if (m>=80):
            bm=(0.08*m)
        elif (m>=60):
            bm=(0.06*m)
        elif (m>=40):
            bm=(0.04*m)
        else :
            bm=(0)
    else :
        if (m>=80):
            bm=(0.06*m)
        elif (m>=60):
            bm=(0.04*m)
        elif (m>=40):
            bm=(0.02*m)
        else :
            bm=(0)
    m=m+bm
    print(m)

print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')

# end of program