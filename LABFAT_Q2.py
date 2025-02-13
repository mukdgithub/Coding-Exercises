'''
	'''
    
#21BCI0003
#MUKUND AGARWAL
pin=1010                                  #assign value of pin as 1010.
amt=5000                                  #asgn value of amount as 5000.
p=int(input('Enter your PIN'))            #inputting pin to start the transactions. 
if (p==pin):                              #check if the input pin matches the pre-stored pin.
    print('Enter your Choice # 1- Balance checking, 2-Cash withdrawal, 3-Cash deposition, 4-Quit.')
    c=int(input())                        #inputting c for the first time.
    while (c!=4):                         #check if c is not '4' to execute remaining iterations.
        if (c==1):                        #check if c is '1' to execute balance checking.
            print(amt)
        elif (c==2):                      #check if c is '2' to execute cash withdrawal.
            w=int(input())
            amt=amt-w
            print(amt)
        elif (c==3):                      #check if c is '3' to execute cash deposition.
            d=int(input())
            amt=amt+d
            print(amt)
        c=int(input())                    #input choice for next iteration.
    print('Thanks for the Transaction')   #printing statement for completing atm transactions.
else:
    print('wrong pin')
#21BCI0003
#MUKUND AGARWAL