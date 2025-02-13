''' problem set 1 Q4
    
    Implement a python code to get the weight and height of a person,
    calculate BMI and print both BMI value and also the appropriate interpretation '''

weight=float(input("Enter the weight : "))
height=float(input("Enter the height : "))
BMI=(weight/(height**2))
print("BMI is : ",BMI)
if BMI<16:
    print("Serious Underweight")
elif 16<=BMI<18:
    print("Underweight")
elif 18<=BMI<24:
    print("Normal Weight")
elif 24<=BMI<29:
    print("Overweight")
elif 29<=BMI<35:
    print("Seriously Overweight")
else:
    print("Gravely Overweight")
# end of program.