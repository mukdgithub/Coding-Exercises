''' Construct a python program to receive a positive number n
    then computes the factorial of all the even numbers between 1 and n,
	if the given n is an even number.
    Same way the factorial of odd numbers between 1 and n,
	if the given n is an odd number.(use while loop)
	
           Test        Input        Result
            1            5           1   1
			                         3   6
									 5   120
									 
    ...module 3 workout Q4...'''

n,a,b,c,f=0,0,2,1,1
n=int(input())
if (n<0) :
    print("invalid input")
else:
    if (n%2==0):
        while (b<=n):
            a=b
            f=1
            while (a>=1):
                f=f*a
                a=a-1
            print(b,f)
            b=b+2
    else :
        while (c<=n):
            a=c
            f=1
            while (a>=1):
                f=f*a
                a=a-1
            print(c,f)
            c=c+2

print('21BCI0003')
print('MUKUND AGARWAL')

# end of program