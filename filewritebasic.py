fh=open('samplewrite.txt','w')
l1=['ram','sita','ganesh']
fh.writelines(l1[][])

for i in range (len(l1)):
    for j in range (len(l1[i])):
        fh.write(str(l1[i][j])
        if (j<(len(l1[i])-1)):
            fh.write(',')
    fh.write('\n')
fh.close()