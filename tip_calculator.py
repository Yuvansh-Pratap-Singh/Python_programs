print(" *** Welcome to the tip calculator *** ")
bill = float(input("What was the total bill ? "))
tip = float(input("What percentage tip would you like to give ? "))
people = int(input("How many people to split the bill ? "))
result = (tip/100*bill+bill)/people
pay = "{:.2f}".format(result)
print("Each person should pay : "+ pay)