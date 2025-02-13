''' [M5_CSQ2]

	A word is called as a good word if all the letters of the word are distinct. That is, all the
	letters of the word are different from each other letter. Else, the word is called as a bad
	word. Write an algorithm and the subsequent Python code to check if the given word is
	good or bad.: e.g. START, GOOD, BETTER are bad: WRONG is good! Make the comparison
	to be case insensitive.         '''

word = input()
word = word.lower()
length = len(word)
count=0
for i in range(0,length):
    for j in range(0,length):
        if word[i]==word[j]:
            count+=1
if count==len(word):
    print('Good')
else:
    print('Bad')
print('21BCI0003')
print('MUKUND AGARWAL')

#END OF PROGRAM