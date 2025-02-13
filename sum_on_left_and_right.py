''' [M4_CSQ1]
    Construct a python program to accept a list of N numbers.
    The job is to determine if there exists
    an element in the list such that the sum of the
    elements on its left is equal to the sum of the elements
    on its right. If such element exists,
    then print the index of the element. If there are no such
    elements, then the sum is zero. [CO1] [L2]
	check if there is a number in the list.         '''

c=0
num=[]                      # creating list.
n=int(input())              # inputting number of values.
num=input().split()         # splitting input values to make their list.
for i in range(1,n-1):
    s1,s2=0,0
    for j in range (i):
        s1+=int(num[j]) 
    for k in range (i+1,n):
        s2+=int(num[k])
    if (s1==s2):
        print(i)
        c+=1
        break
if (c==0):
    print('0')
print('21BCI0003')
print('MUKUND AGARWAL')
# end of program.