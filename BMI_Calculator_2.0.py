height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi = weight/height**2
round_bmi = round(bmi)

if round_bmi < 18.5:
    print(f"Your BMI is : {round_bmi}, you are under weight")
elif round_bmi < 25:
    print(f"Your BMI is : {round_bmi}, you have a normal weight")
elif round_bmi < 30:
    print(f"Your BMI is : {round_bmi}, you are over weight")  
elif round_bmi < 35:
    print(f"Your BMI is : {round_bmi}, you are obese")  
else:
    print("you are clinically obese")       
