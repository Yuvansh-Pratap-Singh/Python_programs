height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi = weight/height**2
int_bmi = int(bmi)

print("Your BMI Index is : "+ str(int_bmi))