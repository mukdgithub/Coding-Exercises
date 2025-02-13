'''[M6_CSQ1]	 
	A string s2 is said to be a “substring” of a string s1, if s2 can be derived from s1 
	by deleting some characters. Given two strings s1, s2 and starting position of the search, 
	develop an algorithm and write a python code to search the substring s2 and 
	print the position of substring in main String s1, if found. 
	Otherwise print “NotAvailable”. [CO2] [L1]     '''

import re
s1=input()
s2=input()
match = re.search(s2,s1)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))

print('21BCI0003')
print('MUKUND AGARWAL')

#end of 