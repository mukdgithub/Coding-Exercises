fh=open('fa.txt','w')
l1=[23,56,44,45]
fh.writelines(l1)
'''
for i in range (len(l1)):
    fh.write(str(l1[i]))
'''
#fh.write('god is great')
fh.close()