# area of triangle from its three sides
a,b,c,s,area=0.0,0.0,0.0,0.0,0.0
import math 
print('enter sides of triangle')
a=float(input())
b=float(input())
c=float(input())
s=((a+b+c)/2)
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
area=round(area,2)

print('\n')
print('21BCI0003')
print('MUKUND AGARWAL')

print(area)