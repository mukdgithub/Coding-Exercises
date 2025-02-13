# multiplication table

import sys
i,n,m,=1,0,0
n=int(input())
m=int(input())
if (n<=0 or m<=0):
    sys.exit()
else:
    while i<=m:
        print("",i," * ",n," = ",(i*n))
        i=i+1
#end of program