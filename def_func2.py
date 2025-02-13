# defining different functions to check the working... 
def add(a,b):
    s=a+b
    return(s)
def sub(a,b):
    s=a-b
    return(s)
def mul(a,b):
    s=a*b
    return(s)
def div(a,b):
    s=a/b
    return(s)
def f1(*args):
    print(args)
def f2(**args):
    print(args)
    print(args.keys())
    print(args.values())
    print(args.items())

m,n=13,12
print('hi')
#f1(m,n,10,34)
#f2(ram=101,sita=102)
f2(a='ram',b='sita')



'''print('do you want to continue')
print('1 to continue, 0 to stop')
op=int(input())
while (op==1):
    print('Enter your choice')
    print('1. for add, 2. for sub, 3. for mul, 4. for div.')
    c=int(input())
    if (c==1):
        print('add result = ',add(m,n))
    elif (c==2):
        print('subtraction result = ',sub(m,n))
    elif (c==3):
        print('multiplication result = ',mul(m,n))
    elif (c==4):
        print('division result = ',div(m,n))
    else:
        print('invalid choice')
'''