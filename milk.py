''' Milk is collected for sales from nearest ‘n’ farms to the milk booth.
    Given the amount of milk from ‘n’ farms in liters and ml.
    Write a PAC chart, algorithm, and flowchart 
    to compute total quantity of milk in the booth.  '''

i=0
milk=[]
n=int(input())
while (i<=n):
    sum=sum+milk[i]
    i=i+1
print(sum)

# end of program