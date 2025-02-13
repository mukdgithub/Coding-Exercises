#army camp recuitment
a=float(input())                           #inputting age
h=float(input())                           #inputting height
w=float(input())                           #inputting weight
c=float(input())                           #inputting chest value
if (a<=18 or a>=25):                      #checking for age
    print('disqualified due to age')
elif (h<=5.2 or h>=5.6):                    #checking for height
    print('disqualified due to height')
elif (w<=45 or w>=60):                      #checking for weight
    print('disqualified due to weight')
elif (c<=45):                                #checking for chest value
    print('disqualified due to chest')
else :
    print('Fit to army')