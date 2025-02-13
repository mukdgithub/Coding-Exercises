# checking input from user in list within dict

d1={}
k=input("enter the key : ")
n=int(input('enter no of elements in a tuple : '))
'''t=()
for i in range (n):
    v=input('enter value : ')
    t[i]=v
d1[k]=t


d1[k]=()'''
t=()
for i in range (n):
    v=input('enter value : ')
    #d1[k][i]=v
    t=t+(v,)
d1[k]=t

print(d1)