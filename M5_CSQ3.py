''' [M5_CSQ3] 
	Construct an algorithm and write a python program to search a literal, string
	in a string and find the location within the original string where the pattern occurs. '''

'''
import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))
'''


import re
text = input()
pattern = input()
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))


'''
import re
s=input()
check=input()   
match = re.search(r(check), s)
print(match.start(),' to ',match.end())
'''