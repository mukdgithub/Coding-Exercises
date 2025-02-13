''' PS3 Q2 
	Write a python program to identify the names and age in the given below string
	using Regex (Regular Expressions) or regular constructs.
	Identified name and age has to be placed a key value pair using dictionary.	'''

import re
x=0
string=str(input())
ages=re.findall('[0,9]+',string)
names=re.findall(r'[A-Z][a-z]*',string)
ageDict={}
for eachname in names:
    ageDict[eachname]=ages[x]
    x+=1
print(ageDict)

#