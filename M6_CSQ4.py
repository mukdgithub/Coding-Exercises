''' [M6_CSQ4] 
    Write a python program to generate a quiz using two files, named Questions.txt and Answers.txt. 
    The program opens Questions.txt and displays the question with options on the screen. 
    The program will verify the Answer.txt file and display the scores.     '''

Questions = open("C:\PythonPrograms\Questions.txt","r")
Answers   = open("C:\PythonPrograms\Answers.txt","r")
Q = (Questions.read()).split("\n")
A = (Answers.read()).split("\n")
Questions.close()
Answers.close()
ans=[]
for r in range(0,len(A)):
    ans.append(A[r][-1])
Res=[]
Score=0
c=0
for r in range(0,len(Q),2):
    print("\n",Q[r])
    print("\t",Q[r+1])
    Flag=1
    while(Flag):
        Res = (str(input('Enter Answer : '))).lower()
        if(Res=="a" or Res=="b" or Res=="c" or Res=="d"):
            Flag=0
    if(Res==ans[c].lower()):
        Score = Score+50
    c=c+1        
print('\n','Score = ',Score)
print('21BCI0003')
print('MUKUND AGARWAL')

#end of 