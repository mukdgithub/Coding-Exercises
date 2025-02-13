''' ProblemSet3_Q1
	Write a python program to find the “kth smallest element”
	in the ascending order sorted list.
	Also check if the given number is present in the list using any searching technique.
	If suppose element to be searched, is not available then display
	“Not Present” otherwise display “Present”.		'''

L=[]
n=int(input())
for i in range (n):
    v=int(input())
    L.append(v)
k=int(input())
key=int(input())
L.sort()

print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')
print(L)
print(L[k-1])
if key in L:
    print('Present')
else:
    print('Not Present')
#end of program