'''
    Metadata
    
    bytes
    created
    owner
    nature of content in the file
'''

'''fh=open("f1.txt","r")
#print(fh.read())
print(fh.readline())
print(fh.readline())
print(fh.readline())
#print(fh.readlines())
fh.close()'''

fh=open("f1.txt","r")
print(fh.read())

'''
fh=open("f1.txt","r")
l1=fh.readlines()
print(l1)
nooflines=len(l1)
print(nooflines)
for i in range (nooflines):
    l2=l1[i].split(' ')
    #print(l2)
    if(int(l2[2])>=18):
        print(l2)
fh.close()
'''