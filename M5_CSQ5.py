''' [M5_CSQ5] 
	Construct an algorithm and write a python program python program to create
	a regular expression to retrieve all words starting with vowels in each string.  '''

test_list = input().split()
res = []
vow = "aeiou"
for sub in test_list:
	flag = False
	for ele in vow:
		if sub.startswith(ele):
			flag = True
			break
	if flag:
		res.append(sub)
print(str(res))
print('21BCI0003')
print('MUKUND AGARWAL')

#end of program