#square matrix
'''
m=int(input())
n=int(input())
if (m<=0 or n<=0 or not m==n):
    print('invalid input')
else:
    for i in range (n):
        for j in range (n):
            arr[i][j]=int(input())
            if (i==j):
                d1=d1+int(arr[i][j])
            if (i==n-j-1):
                d2=d2+int(arr[i][j])
    abs_diff=abs(d1-d2)
    for k in range (n):
        for l in range (n):
            value=arr[l][k]
            print(value)'''


'''dic={}
d1=0, d2=0
m=int(input())
n=int(input())
if (m<=0 or n<=0 or not m==n):
    print('invalid input')
else:
    for i in range (n):
        for j in range (n):
            dic[i]=[]
            v=int(input())
            dic[i].append(v)
            if (i==j):
                d1=d1+v
            if (i==n-j-1):
                d2=d2+v
    print(d1)
    print(d2)
    d=d1-d2
    print(abs(d))'''
    
'''   
a=0
b=0
dic={}
m=int(input())
n=int(input())
if (m<=0 or n<=0 or not m==n):
    print('invalid input')
else:
    for i in range (n):
        for j in range (n):
            dic[i]=[]
            v=int(input())
            dic[i].append(v)
            if (i==j):
                a+=v
            if (i==n-j-1):
                b+=v
    print(a)
    print(b)
    print(abs(a-b))
    print(dic)
'''

a=0
b=0
dic={}                           #initialising dictionary
m=int(input())                   #inputting rows
n=int(input())                   #inputting columns
if (m<=0 or n<=0 or not m==n):   #checking boundary conditions
    print('invalid input')
else:
    for i in range (n):
        for j in range (n):
            dic[i]=[]
            v=int(input())        #inputting matrix values
            dic[i].append(v)
            if (i==j):
                a+=v
            if (i==n-j-1):
                b+=v
    print(a)                      #printing sum of first diagonal
    print(b)                      #printing sum of second diagonal
    print(abs(a-b))               #printing absolute difference