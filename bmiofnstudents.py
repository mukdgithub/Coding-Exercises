#calculate BMI for n students

height,weight,BMI,i,n=0.0,0.0,0.0,1,0
n=int(input("Enter the total number of Students : "))
while i<=n:
    if i==1:
        height=float(input("Enter the height of the Student : "))
        weight=float(input("Enter the weight of the Student : "))
    else :
        height=float(input("Enter the height of next Student : "))
        weight=float(input("Enter the weight of next Student : "))
    BMI=(weight/(height**2))
    print("The BMI is",BMI)
    i=i+1
print("Calculation of BMI is finished.")

#end of program