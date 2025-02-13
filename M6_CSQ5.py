''' [M6_CSQ5] 
	Write a python program that defines a user defined function called frequency () which 
    identifies and count the frequency of occurrences of the words in a given sentence 
    that is passed to the user defined function. The frequency occurrences of the word 
    should be returned in sorted order by words in the string.      '''

def frequency(L):
    for i in range (len(L)):
        count=0
        for j in range (len(L)):
            if (L[i]==L[j]):
                count+=1
        print('',L[i],':',count)

L=[]
L=input().split()
frequency(L)

print('\n')
print(' 21BCI0003')
print(' MUKUND AGARWAL')

# end of p