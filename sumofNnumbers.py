#Sum of n numbers

n,sum,i=0,0.0,1
n = int(input("Enter the quantity of numbers to be added "))
while i<=n:
    num = float(input("Enter the number "))
    sum=sum+num
    i=i+1
print("Sum is ",sum)

#end of program