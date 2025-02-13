'''[M6_CSQ2] 
	Develop a program using function to solve a classic ancient puzzle.  
	We count m heads and n legs among chickens and rabbits in a farm. 
	How many rabbits (x) and chickens (y) do we have? If m and n are 35 and 94, 
	then the x and y will be 12 and 23. [CO2] [L1]          '''

m = int(input())
n = int(input())
c = (n-(2*m))//2
r = m-((n-(2*m))//2)
print(c)
print(r)
print('21BCI0003')
print('MUKUND AGARWAL')

# end of program