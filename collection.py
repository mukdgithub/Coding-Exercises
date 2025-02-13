#sum of n numbers

n,sum=0,0
n=int(input())
L1=[]
for i in range(n):
    val=int(input())
    L1.append(val)
for i in range(n):
    sum=sum+L1[i]
print(L1)
print("sum = ",sum)
for i in range(n):
    print(" L1 [",i,"] is ",L1[i])
#end of program