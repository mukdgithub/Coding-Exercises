'''
input string 
output int
from ROHIT 
input = '123'
output = 123
''' 
s=str(input())
l=len(s)
if s[0]=="'" and s[-1]=="'":
    d=''
    for i in range(1,l-1):
        d=d+s[i]
print(int(d))