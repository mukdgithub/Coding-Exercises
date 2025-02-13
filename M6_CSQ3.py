''' [M6_CSQ3]	 
	Design a python program to list the students’ name who secured 
	(i)	exact mean score
	(ii)	above mean score and 
	(iii)	below mean score 
	of the class using user defined function           '''

'''
s1,m1=input().split()
s2,m2=input().split()
s3,m3=input().split()

m1=int(m1)
m2=int(m2)
m3=int(m3)
avg=(m1+m2+m3)/3

if (m1==avg):
    print(s1,end=' ')
if (m2==avg):
    print(s2,end=' ')
if (m3==avg):
    print(s3,end=' ')
print('\n')
if (m1>avg):
    print(s1,end=' ')
if (m2>avg):
    print(s2,end=' ')
if (m3>avg):
    print(s3,end=' ')
print('\n')
if (m1<avg):
    print(s1,end=' ')
if (m2<avg):
    print(s2,end=' ')
if (m3<avg):
    print(s3,end=' ')

print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')
'''
def marks(s1,m1,s2,m2,s3,m3):
    m1=int(m1)
    m2=int(m2)
    m3=int(m3)
    avg=(m1+m2+m3)/3

    if (m1==avg):
        print(s1,end=' ')
    if (m2==avg):
        print(s2,end=' ')
    if (m3==avg):
        print(s3,end=' ')
    print('\n')
    if (m1>avg):
        print(s1,end=' ')
    if (m2>avg):
        print(s2,end=' ')
    if (m3>avg):
        print(s3,end=' ')
    print('\n')
    if (m1<avg):
        print(s1,end=' ')
    if (m2<avg):
        print(s2,end=' ')
    if (m3<avg):
        print(s3,end=' ')

s1,m1=input().split()
s2,m2=input().split()
s3,m3=input().split()

marks(s1,m1,s2,m2,s3,m3)

print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')



# end of 