''' Construct a python program to calculate sum of digits of a given number
    until the sum becomes a single digit number. (Using loop).
           
           Test    Input    Result
             1      234       9
             
    module 3 workout Q5  '''

n,r,sum=0,1,0
n=int(input())
while ( n>0 or sum>9 ):
    if (n==0):
        n=sum
        sum=0
    sum=sum+(n%10)
    n=n//10
    
print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')

print(sum)

# end of program