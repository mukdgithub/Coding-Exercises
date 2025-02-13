''' problem set 1 Q2

	Calculate the Average of 'N' numbers '''

i,n,num,sum,avg=1,0,0.0,0.0,0.0
n=int(input())
while i<=n:
    num=float(input())
    sum=sum+num
    i=i+1
average=(sum/n)
print(average)

# end of program.