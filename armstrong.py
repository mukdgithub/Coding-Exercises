# check armstrong number

num,sum,rem,quo,=0,0,0,0
num=int(input())
num1=num
while num>0:
    quo=num//10
    rem=num%10
    sum=sum+pow(rem,3)
    num=quo
if (num1==sum):
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
# end of program.