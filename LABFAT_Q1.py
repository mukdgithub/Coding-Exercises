'''
	'''

#21BCI0003
#MUKUND AGARWAL
def biggest(L):
    max=L[0]
    for j in range(1,len(L)):
        if (L[j]>max):
            max=L[j]
    print(max)

L=[]
size=int(input())
for i in range(size):
    value=int(input())
    L.append(value)
biggest(L)
#21BCI0003
#MUKUND AGARWAL