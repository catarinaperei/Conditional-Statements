height=float(input("enter your height m"))
weight=float(input("enter your weight in kg"))
BMI=weight/(height**2)

if BMI<18.5:
    print("you are under weight")
elif BMI<24.9:  
    print("you are normal weight") 
elif BMI<25:   
    print("overweight")
elif BMI<30:
    print("obese")
else:
    print("extremely obese")