"""for loop for pattern and sum of all the displayed numbers
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5  and so on....  """

i,r,n,sum=1,0,1,0
r=int(input("Enter the number of rows to be printed : "))
print("\n")
        print(" ",n, end="")
        sum=sum+n
        n=n+1
    i=i+1
    n=1
    print("\n")
print("The Sum of all the numbers is : ",sum)

#end of program