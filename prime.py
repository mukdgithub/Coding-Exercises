# prime number or not

i=2,flag=0
num=input(())
if (num<2):
while (i<num):
	if (num%i==0):
        flag=1
        break
    i=i+1
    if (flag==1)
        print(" not prime ")
    else:
        print(" prime ")
# end of program