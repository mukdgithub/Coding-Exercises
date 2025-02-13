# problem set2 Q2.

''' There are ‘n’ players list released indicating the players being
    selected in Indian team for ICC world cup T20 tournament.
    a) The board decides to release the players in alphabetical order of their names.
    b) The ICC board decides to release the players in decreasing order of their batting 
    average rates.
    c) The board decides to release the topper in the team based on Batting Average Rate.
    
    Note: If boundary conditions are not met, then print ‘Invalid Input’.
    
    Input format...
    - First line contains the value of ‘n’
    - Next ‘n’ lines contain the details of ‘n’ players in the format
      : name of the player, batting average separated by a comma.
    
    Output Format...
    - Print the name of the players in alphabetical order.
    - Print the name of the players in highest to lowest order of batting average.
    - Print the topper in the team with highest batting average.         '''

name=[]                                  #creating list "name"
rate=[]                                  #creating list "rate"
n=int(input())                           #inputing no. of players
if (n<=0) :                              #checking boundary condition
    print("Invalid Input")
else :
    for i in range (n):
        a,b=input().split(",")           #splitting input with comma
        name.append(a)
        rate.append(b)
    name.sort(), rate.sort(reverse=True) #sorting both lists
    print(name)                          #printing names in alphabetical order
    print(rate)                          #printing batting average in descending order
    print(rate[0])                       #printing topper of team