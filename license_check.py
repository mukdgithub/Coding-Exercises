# problem set2 Q1.

''' LicenseNo   Name    Previous License Issued Dates   Gender
    101          A              1/01/2008                Male
    102          B              1/01/2010               Female
    103          C              5/01/1996               Female
    104          D              6/06/1996                Male
    105          E              5/06/2015                Male           '''
''' Write Python program to find 
    a) Display LicenseNo’s of the people who are Male
    b) Display  Name of the people who are Female
    c) Accept License Expiry term ( namely 'x' ) 
       which is the term period after which a renewal is to be done 
       to continue for an active license status.
       Identify those LicenseNo’s that fall in this category.
       Rightly these license no's will be the people
       for whom their license has got expired and will now be crossing
       beyond or equal to this ‘x’ yrs term period from
       issue date as mentioned in the above table
    d) Accept a month and Display the Names of people  
       who have commonality in the Issued months.                       '''
''' INPUT FORMAT:
        License Expiry Term 'x'  (eg 10 years).
        Month to check for commonality.
    OUTPUT FORMAT:
        LicenseNo’s of the people who are Male.
        Name of the people who are Female.
        LicenseNo’s that are now equal or more than ‘x’ yrs from issue date.
        Names of people who have commonality in the previous license Issued months.  '''

license_no=(101,102,103,104,105)
name=('A','B','C','D','E')
date=('1/01/2008','1/01/2010','5/01/1996','6/06/1996','5/06/2015')
gender=('Male','Female','Female','Male','Male')
term=int(input())                      #inputting expiry term.
mon=int(input())                       #inputting commonality month.
for i in range (5):
    if (gender[i]=='Male'):  
        print(license_no[i],end=' ')   #printing lic no. of male.
print('\n')
for j in range (5):
    if (gender[j]=='Female'):
        print(name[j],end=' ')         #printing name of female.
print('\n')
for k in range (5):
    date_tuple=date[k]                 #extracting date from tuple.
    year=date_tuple[5:9]               #extracting year from date.
    year=int(year)                     #converting string(year) to int(year).
    if ((year+term)<=2021):
        print(license_no[k],end=' ')   #printing lic no. which are expired.
print('\n')
for l in range (5):
    month_tuple=date[l]                #extracting date from tuple.
    month=month_tuple[2:4]             #extracting month from date.
    month=int(month)                   #converting string(month) to int(month).
    if (month==mon):
        print(name[l],end=' ')         #printing name of people with commonality.
# end of program.